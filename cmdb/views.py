from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from cmdb.serializer import ResourceSerializer,UserSerializer,UserDetailSerializer,CommentSerializer,CommentCreateSerializer,UserCreateSerializer,UserInfoSerializer
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.core import serializers as dcs
from Monstagram_backend.helper import apiTest,md5

# 作品总列表接口
class ResourceList(APIView):
    # 这里一定要注意 每个方法里必须包括request参数
    # 这里多表联合查询时我们可以将其分解为两部分
    def get(self,request,format=None):
        uid = request.GET.get("user_id")
        import time
        resource = models.Resources.objects.all().order_by("-created_at")
        # 添加昵称
        nickname_list = []
        for x in resource:
            nickname_list.append(x.user.nickname)
        serializer = ResourceSerializer(resource,many=True)
        result = []
        num = 0
        for item in serializer.data:
            item['nickname'] = nickname_list[num]
            # 计算点赞数
            item['praise_num'] = models.UserLikes.objects.filter(resources_id=item['id']).count()
            item['praise_check'] = models.UserLikes.objects.filter(resources_id=item['id'],user_id=uid).count()

            comment_data = models.UserComment.objects.filter(resources_id = item['id'])
            comment_serializer = CommentSerializer(comment_data,many=True)
            item['comment'] = comment_serializer.data
            # 计算时间差
            now_time = int(time.time())
            time_diff_seconds = now_time - item['created_at']
            time_diff_day = int(time_diff_seconds / 60 / 60 / 24)
            time_diff_hours = int(time_diff_seconds / 60 / 60)
            time_diff_minutes = int(time_diff_seconds / 60)

            if (time_diff_day > 0):
                item['time_diff'] = str(time_diff_day) + ' 天'
            elif (time_diff_hours > 0):
                item['time_diff'] = str(time_diff_hours) + ' 时'
            elif (time_diff_minutes > 0):
                item['time_diff'] = str(time_diff_minutes) + ' 分'
            else:
                item['time_diff'] = str(time_diff_seconds) + ' 秒'

            result.append(item)
            num += 1
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
        # 添加创建时间和更新时间
        import time
        request.data['created_at'] = int(time.time())
        request.data['updated_at'] = int(time.time())
        request.data['status'] = 1
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 用户总列表接口
class User(APIView):

    def get(self,request,format=None):
        user = models.User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        # 添加创建时间和更新时间
        import time
        request.data['created_at'] = int(time.time())
        request.data['updated_at'] = int(time.time())
        # 这里对密码进行md5
        request.data['password'] = md5(request.data['password'])
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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

# 评论
class CommentList(APIView):

    def get(self,request,format=None):
        comment = models.UserComment.objects.all()
        serializer = CommentSerializer(comment,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        # 添加创建时间和更新时间
        import time
        request.data['created_at'] = int(time.time())
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 登录
class Login(APIView):

    def post(self,request,format=None):
        try:
            info = models.User.objects.get(email=request.data['email'])
        except Exception as e:
            return apiTest({'status':0,'message':'用户不存在！'})

        user_password_md5 = md5(request.data['password'])
        if (info.password == user_password_md5):
            return apiTest({'status':1,'message':'登录成功！','data':{'user_id':info.id,'nickname':info.nickname}})
        else:
            return apiTest({'status':0,'message':'密码错误！',})

class Praise(APIView):

    def post(self,request,format=None):
        import time
        create_at = int(time.time())
        user_praise = models.UserLikes.objects.create(user_id=request.data['user_id'],resources_id=request.data['resources_id'],created_at=create_at)
        if (user_praise):
            return apiTest({'status':1,'message':'操作成功！'})
        else:
            return apiTest({'status':0,'messaga':'操作失败！'})

class PraiseCancel(APIView):

    def delete(self,request,format=None):
        status = models.UserLikes.objects.filter(user_id=request.data['user_id'],resources_id=request.data['resources_id']).delete()
        if (status):
            return apiTest({'status':1,'message':'操作成功！'})
        else:
            return apiTest({'status':0,'messaga':'操作失败！'})

