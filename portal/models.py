from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Building(models.Model):
    cityName = models.CharField(max_length=100)
    streetName = models.CharField(max_length=100)
    houseNumber = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.cityName}, {self.streetName}, {self.houseNumber}'


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None, null=False)
    telephone = models.CharField(max_length=30, null=True)
    flatNumber = models.IntegerField(null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)

    def __str__(self):
        pass
        return self.user.username


class Counter(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    coldWater = models.IntegerField()
    hotWater = models.IntegerField()
    electricity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.building}, кв.{self.profile.flatNumber} | {self.date}"