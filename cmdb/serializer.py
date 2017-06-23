from rest_framework import serializers
from . import models

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resources
        fields = ('id','title','img_url','created_at','status')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','email','nickname','prefix','phone','created_at','updated_at')
        # exclue = ('users',)
        # read_only_fields = ('email',)