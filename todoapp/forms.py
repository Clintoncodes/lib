from django import forms
from .models import MyTodo

class MyTodoForm(forms.ModelForm):
    hobby = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id':'todoField', 'placeholder':"Enter Task"
    }))
    class Meta:
        model = MyTodo
        fields = ['hobby',]