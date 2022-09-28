from django import forms
from .models import Tasks
from django.contrib.auth.models import User

class Task_form(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

