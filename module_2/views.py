from django.shortcuts import render
from .models import QnA
from .forms import CREATE_QNA
from django.views.generic import ListView

# Create your views here.
def create_question(request):
    forms =CREATE_QNA(request.POST or None)
    if forms.is_valid():
        forms.save()
    context={
        "forms":forms
    }
    return render(request,"qna.html",context)

class view_question(ListView):
    model= QnA
    template_name = "qna_view.html"

def home_page(request,*args,**kwargs):
    return render(request,"homepage.html",{})