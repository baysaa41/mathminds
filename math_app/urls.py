from django.urls import path

from math_app.models import AnswerChoice
from problems.views import ProblemDetail, AnswerChoiceDetail

urlpatterns = [
    path('problems/<int:pk>/', ProblemDetail.as_view(), name='problem-detail'),
    path('answerchoices/<int:pk>/', AnswerChoiceDetail.as_view(), name='answer-choice-detail'),
]
