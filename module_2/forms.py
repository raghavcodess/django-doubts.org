from django import forms
from .models import QnA

class CREATE_QNA(forms.ModelForm):
    class Meta:
        model=QnA
        fields =[
            'desription', 
            'author'
            ]