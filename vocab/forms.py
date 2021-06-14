from django import forms
from django.forms.models import ModelChoiceField
from .models import Word
from django.forms import ModelForm
from django.utils.safestring import mark_safe

class wordform(ModelForm):
    class Meta:
        model = Word
        exclude = []

    parent = ModelChoiceField(queryset = Word.objects.all())