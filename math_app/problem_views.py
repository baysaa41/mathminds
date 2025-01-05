from django.shortcuts import render, get_object_or_404, redirect
from .models import Problems, AnswerChoice
from .forms import ProblemForm, AnswerChoiceForm

def problem_editor(request, pk=None):
    problem = get_object_or_404(Problems, pk=pk) if pk else None
    if request.method == "POST":
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('problem_list')
    else:
        form = ProblemForm(instance=problem)
    return render(request, 'problem_editor.html', {'form': form, 'problem': problem})
