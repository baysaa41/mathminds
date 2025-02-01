from django.urls import path
from problems.views import problem_editor, ProblemSearch

urlpatterns = [
    path('<int:pk>/edit/', problem_editor, name='edit_problem'),
    path('create/', problem_editor, name='create_problem'),
    path('search/', ProblemSearch.as_view(), name='search_problem'),
]