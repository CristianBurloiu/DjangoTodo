from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ('name', )
        
class EditTodoItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ('name', 'done')