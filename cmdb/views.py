from django.shortcuts import render
from . import models
import time
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from cmdb.serializer import ResourceSerializer,UserSerializer
from django.http import Http404

class ResourceList(APIView):

    def get(self,request,format=None):
        resource = models.Resources.objects.all()
        serializer = ResourceSerializer(resource,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REAQUEST)

class UserDetail(APIView):

    def get_object(self,pk):
        try:
            return models.User.objects.get(pk=pk)
        except models.User.DoesNotExist:
            raise Http404


    def get(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)