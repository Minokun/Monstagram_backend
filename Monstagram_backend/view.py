from django.shortcuts import render
from django.http import HttpResponse
import os
from Monstagram_backend.helper import apiTest

def index(request):
    return render(request,'upload.html')

# 上传文件
def upload_file(request):

    if request.method == "POST":
        try:
            myFile = request.FILES.get("avatar", None)
            current_url = "http://" + request.get_host() + "/static/" + myFile.name
            if not myFile:
                return HttpResponse("no files for upload!")
            destination = open(
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common_static', myFile.name),
                'wb+')
            for chunk in myFile.chunks():
                destination.write(chunk)

            destination.close()
            return apiTest({'status': 1, 'pic_url': current_url})
        except Exception as e:
            return apiTest({'status': 0, 'error': e})