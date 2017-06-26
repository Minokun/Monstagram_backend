from rest_framework import serializers
from . import models

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resources
        fields = ('id','user_id','title','img_url','created_at','updated_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','email','nickname','prefix','phone','created_at','updated_at')

class UserDetailSerializer(serializers.ModelSerializer):
    resources_set = ResourceSerializer(many=True, read_only=True)
    class Meta:
        model = models.User
        fields = ('id','email','nickname','prefix','phone','created_at','updated_at','resources_set')
        # exclue = ('users',)
        # read_only_fields = ('email',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserComment
        fields = ('user_id','content','created_at')