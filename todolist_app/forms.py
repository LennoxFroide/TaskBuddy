from django import forms
from todolist_app.models import TaskMate


class TaskForm(forms.ModelForm):     
    class Meta:
        model = TaskMate
        fields = ['task','done']
    
