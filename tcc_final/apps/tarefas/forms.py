from django import forms

class IdForm(forms.Form):
    task_id = forms.CharField(max_length=255)