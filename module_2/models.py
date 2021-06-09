from django.db import models


class QnA(models.Model):
    desription  =   models.TextField()
    author      =   models.CharField(max_length=69,default="anonymous")
    doctor      =   models.CharField(max_length=69,default="not answered yet")
    answer      =   models.TextField(default="not answered yet")

