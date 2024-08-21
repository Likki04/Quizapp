from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Category, Question
import random

from .models import Question  # Assuming you have a Question model
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def Quizapp(request):
    categories = Category.objects.all()
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'home.html', {'categories': categories})

def quiz(request):
    context={'category':request.GET.get('category')}
    return render(request, 'quiz.html',context)

# def get_quiz(request):
#     try:
#         question_objs = Question.objects.all()
#         if request.GET.get('category'):
#             category_name = request.GET.get('category')
#             print(f"Category: {category_name}")  # Debug print
#             question_objs = question_objs.filter(category__category_name__icontains=category_name)
#         question_objs = list(question_objs)  # Convert to list after filtering
#         data = []
#         random.shuffle(question_objs)
#         print(f"Questions: {question_objs}")  # Debug print
#         for question_obj in question_objs:
#             answers = question_obj.get_answers()
#             print(f"Question: {question_obj.question}, Answers: {answers}")  # Debug print
#             data.append({
#                 "category": question_obj.category.category_name,
#                 "question": question_obj.question,
#                 "marks": question_obj.marks,
#                 "answers": answers
#             })
#         payload = {'status': True, 'data': data}
#         return JsonResponse(payload)
#     except Exception as e:
#         print(f"Error: {e}")  # Detailed error message
#         return HttpResponse("Something went wrong")
def get_quiz(request):
    category = request.GET.get('category', None)
    if category:
        questions = Question.objects.filter(category__name=category).values('id', 'text', 'options')
        # Assuming 'options' is a JSON field in your Question model or a related model.
        # Adjust accordingly if your structure is different.
    else:
        questions = Question.objects.all().values('id', 'text', 'options')

    questions_list = list(questions)  # Convert queryset to list
    data = {
        'data': questions_list
    }
    return JsonResponse(data)
