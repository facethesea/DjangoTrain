import imp
from django.http import JsonResponse
from django.shortcuts import render
from sqlite3Exp.models import BaseInfo
from django.http import JsonResponse
# Create your views here.
def addinfo(request):
    name=request.GET('neme')
    age=int(request.GET('age'))
    BaseInfo.objects.create(姓名=vname,年龄=vage)
    return JsonResponse({'code':0,'message':'成功添加了一条学生记录'})
