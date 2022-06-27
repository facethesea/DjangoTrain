from operator import mod
from django.db import models

# Create your models here.
#
#
#
#
class BaseInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,name='姓名')
    age=models.SmallIntegerField(nmae='年龄')

class Hbby(models.Model):
    id=models.AutoField(primary_key=True)
    hobby=models.CharField(max_length=100,name='爱好')
    stuid=models.ForeignKey(BaseInfo,on_delete=models.CASCADE)