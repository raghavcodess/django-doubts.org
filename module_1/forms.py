from django import forms
from .models import NoticeBoard

class CREATE_NOTICE(forms.ModelForm):
    class Meta:
        model=NoticeBoard
        fields =[
            'title', 
            'desription', 
            'author'
            ]
        