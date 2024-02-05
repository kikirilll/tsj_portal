from rest_framework import serializers
from django.contrib.auth.models import User
from portal.models import UserProfile, Counter, Building

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user_id', 'flatNumber', 'building_id')


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ('id', 'coldWater', 'hotWater', 'electricity', 'profile', 'date')


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('id', 'cityName', 'streetName', 'houseNumber')