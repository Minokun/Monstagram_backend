from django.shortcuts import render
from django.http import HttpResponse
from . import models
import time

# Create your views here.
def index(request):
    userObject =models.User.objects.get(pk=1)
    userObject.created_at = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(userObject.created_at))
    return render(request,'cmdb/index.html',{'name': userObject.created_at})