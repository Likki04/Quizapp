from django.urls import path
from .import views
from .views import get_quiz

urlpatterns = [
    path('',views.Quizapp,name="Quizapp"),
    path('api/get-quiz/',get_quiz,name="get_quiz"),
    path('quiz/',views.quiz,name="quiz")
]