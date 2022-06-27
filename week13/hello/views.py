import re
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def GetName(request):
    return HttpRequest("my name is admin")