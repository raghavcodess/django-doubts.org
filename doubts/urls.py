"""doubts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from module_1 import views as x
from module_2 import views as y

urlpatterns = [
    path('', y.home_page , name='home'),
    path('create_notice', x.create_notice , name='notice'),
    path('view_notice', x.NoticeView.as_view() , name='vnotice'),
    path('create_question', y.create_question , name='question'),
    path('view_question', y.view_question.as_view() , name='vquestion'),
    path('admin/', admin.site.urls),
]
