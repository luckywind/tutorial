# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       miranda
   date：          2019/4/23
-------------------------------------------------
   Change Activity:
                   2019/4/23:
-------------------------------------------------
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')