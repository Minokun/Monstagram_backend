from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request,'upload.html')

# 上传文件
def upload_file(request):
    if request.method == "POST":
        myFile = request.FILES.get("myfile",None)

        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'templates/uploadFile',myFile.name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)

        destination.close()
        return HttpResponse("upload over!")