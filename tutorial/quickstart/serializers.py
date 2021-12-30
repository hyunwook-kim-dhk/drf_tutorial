from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tutorial.quickstart.models import Schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['user', 'start_datetime', 'end_datetime', 'summary', 'description', 'tags']
