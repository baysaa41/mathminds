from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from math_app.models import Problems, AnswerChoice
from .forms import ProblemForm, AnswerChoiceForm
from math_app.serializers import ProblemSerializer, AnswerChoiceSerializer
from rest_framework import generics

def problem_editor(request, pk=None):
    problem = get_object_or_404(Problems, pk=pk) if pk else None
    if request.method == "POST":
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            saved_problem = form.save()  # Save the problem

            # Handle AnswerChoice if problem type is not 0
            if saved_problem.type != 0:
                # Remove selected choices
                choices_to_remove = request.POST.getlist('remove_choice')
                if choices_to_remove:
                    AnswerChoice.objects.filter(id__in=choices_to_remove).delete()

                # Update existing choices
                for choice in saved_problem.choices.all().order_by('label'):
                    choice.label = request.POST.get(f'label_{choice.id}', choice.label)
                    choice.value = request.POST.get(f'value_{choice.id}', choice.value)
                    choice.default_score = request.POST.get(f'default_score_{choice.id}', choice.default_score)
                    choice.description = request.POST.get(f'description_{choice.id}', choice.description)
                    choice.save()

                # Add new choices
                new_labels = request.POST.getlist('new_label')
                new_values = request.POST.getlist('new_value')
                new_default_scores = request.POST.getlist('new_default_score')
                new_descriptions = request.POST.getlist('new_description')

                for label, value, score, description in zip(new_labels, new_values, new_default_scores, new_descriptions):
                    if label and value:  # Ensure required fields are provided
                        AnswerChoice.objects.create(
                            problem=saved_problem,
                            label=label,
                            value=value,
                            default_score=score or 0,
                            description=description or ''
                        )

            return redirect('edit_problem', pk=saved_problem.id)
    else:
        form = ProblemForm(instance=problem)
    return render(request, 'problem_editor.html', {'form': form, 'problem': problem})

class ProblemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problems.objects.all()
    serializer_class = ProblemSerializer

class AnswerChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerChoice.objects.all()
    serializer_class = AnswerChoiceSerializer