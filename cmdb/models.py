# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Resources(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    title = models.CharField(max_length=250, blank=True, null=True)
    img_url = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resources'


class User(models.Model):
    email = models.CharField(max_length=45, blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    prefix = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserComment(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    resources = models.ForeignKey(Resources, models.DO_NOTHING)
    content = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_comment'


class UserLikes(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    resources = models.ForeignKey(Resources, models.DO_NOTHING)
    created_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_likes'
