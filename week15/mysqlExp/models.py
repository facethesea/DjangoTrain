from re import T
from typing import ChainMap
from django.db import models
from django.forms import CharField

# Create your models here.
class BaseInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.SmallAutoField()


class Hobby(models.Model):
    id=models.AutoField(primary_key=True)
    hobby=models,CharField(max_length=200)
    stuid=models.ForeignKey(BaseInfo,on_delete=models.CASCADE)