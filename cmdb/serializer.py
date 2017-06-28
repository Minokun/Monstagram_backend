from rest_framework import serializers
from . import models

class ResourceSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = models.Resources
        fields = ('id','user_id','title','img_url','created_at','updated_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','email','nickname','prefix','phone','created_at','updated_at')

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','password','email','nickname','prefix','phone','created_at','updated_at')

class UserDetailSerializer(serializers.ModelSerializer):
    resources_set = ResourceSerializer(many=True, read_only=True)
    class Meta:
        model = models.User
        fields = ('id','email','nickname','prefix','phone','created_at','updated_at','resources_set')
        # exclue = ('users',)
        # read_only_fields = ('email',)


class CcSerializer(serializers.RelatedField):
    def to_representation(self,value):
        result = {}
        result['email'] = value.email
        result['nickname'] = value.nickname
        result['phone'] = value.phone
        result['created_at'] = value.created_at
        return result

# 评论查询
class CommentSerializer(serializers.ModelSerializer):
    user = CcSerializer(read_only=True)
    class Meta:
        model = models.UserComment
        fields = ('id','user_id','resources_id','content','created_at','user')
        depth = 1

# 评论插入
class CommentCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    resources_id = serializers.IntegerField()
    class Meta:
        model = models.UserComment
        fields = ('id','user_id', 'resources_id', 'content', 'created_at')