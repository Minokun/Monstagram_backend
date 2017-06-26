from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from cmdb.serializer import ResourceSerializer,UserSerializer,UserDetailSerializer,CommentSerializer
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.core import serializers as dcs

# 作品总列表接口
class ResourceList(APIView):
    # 这里一定要注意 每个方法里必须包括request参数
    # 这里多表联合查询时我们可以将其分解为两部分
    def get(self,request,format=None):
        resource = models.Resources.objects.all()
        serializer = ResourceSerializer(resource,many=True)
        result = []
        for item in serializer.data:
            comment_data = models.UserComment.objects.filter(resources_id = item['id'])
            comment_serializer = CommentSerializer(comment_data,many=True)
            item['content'] = comment_serializer.data
            result.append(item)
        return Response(result)

        # sql = """
        #     select
        #         *
        #     from
        #         resources r left join
        #         (select uc.id ucid,u.nickname from user_comment uc left join user u on uc.user_id = u.id) as cu
        #     on r.id = cu.ucid
        # """
        # result = models.Resources.objects.raw(sql)
        # return HttpResponse(dcs.serialize('json',result))

    def post(self,request,format=None):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REAQUEST)

# 用户总列表接口
class User(APIView):

    def get(self,request,format=None):
        user = models.User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REAQUEST)

# 用户详情接口
class UserDetail(APIView):

    def get_object(self,pk):
        try:
            return models.User.objects.get(pk=pk)
        except models.User.DoesNotExist:
            raise Http404


    def get(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def patch(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentList(APIView):
    def get(self,request,format=None):
        comment = models.UserComment.objects.all()
        serializer = CommentSerializer(comment,many=True)
        return Response(serializer.data)