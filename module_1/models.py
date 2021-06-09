from django.db import models
from django.contrib.auth.models import User


class NoticeBoard(models.Model):
    title       =   models.CharField(max_length=69)
    desription  =   models.TextField(default="")
    author      =   models.CharField(max_length=69,default="anonymous")
    

    