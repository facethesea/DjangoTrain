from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class xiaoqu_wailai(models.Model):
    wailai_id=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=12,null=True)
    age=models.IntegerField()
    yezhu_id=models.CharField(max_length=12)