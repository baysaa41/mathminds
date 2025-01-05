from django import forms
from .models import Problems, AnswerChoice

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = ['title', 'type', 'statement', 'rendering', 'level', 'answer', 'mute_comments', 'is_published']

class AnswerChoiceForm(forms.ModelForm):
    class Meta:
        model = AnswerChoice
        fields = ['label', 'value', 'description', 'default_score']
