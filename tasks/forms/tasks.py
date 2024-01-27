from django import forms

class CreateTask(forms.Form):
  title = forms.CharField(
    label='',
    widget=forms.TextInput(

      attrs={
        'placeholder': 'Escribe una tarea...',
        'class': 'p-2 rounded-lg w-full border border-slate-200'
      }
    )
  )
