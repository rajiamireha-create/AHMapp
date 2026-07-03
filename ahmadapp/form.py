from django import forms
from ahmadapp.models import ahmadapptask

class ahmadapptaskform(forms.ModelForm):
    class Meta:
        model = ahmadapptask
        fields = ['task_name','done']
        