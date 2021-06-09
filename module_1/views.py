from django.shortcuts import render
from .models import NoticeBoard
from .forms import CREATE_NOTICE
from django.views.generic import ListView

# Create your views here.
def create_notice(request):
    forms =CREATE_NOTICE(request.POST or None)
    if forms.is_valid():
        forms.save()
    context={
        "forms":forms
    }
    return render(request,"notice.html",context)


class NoticeView(ListView):
    model = NoticeBoard
    template_name = "noticeview.html"

