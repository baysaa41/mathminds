from django import forms
from math_app.models import Problems, AnswerChoice

from django.utils.translation import gettext_lazy as _

class ProblemForm(forms.ModelForm):
    TYPE_CHOICES = [
        (0, _("Уламжлалт")),  # Translate these into Mongolian as needed
        (1, _("Сонгох")),
        (4, _("Нөхөх")),
    ]

    type = forms.ChoiceField(choices=TYPE_CHOICES, label=_("Хэлбэр"))

    class Meta:
        model = Problems
        fields = ['title', 'type', 'statement', 'rendering', 'level', 'answer', 'is_published']
        labels = {
            'title': _("Гарчиг"),
            'statement': _("Өгүүлбэр"),
            'rendering': _("Дүрслэл"),
            'level': _("Түвшин"),
            'answer': _("Зөв хариу"),
            'is_published': _("Нийтлэх эсэх"),
        }


class AnswerChoiceForm(forms.ModelForm):
    class Meta:
        model = AnswerChoice
        fields = ['label', 'value', 'description', 'default_score']
        labels = {
            'label': _("Шошго"),
            'value': _("Утга"),
            'description': _("Тайлбар"),
            'default_score': _("Үндсэн оноо"),
        }