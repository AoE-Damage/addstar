from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bloggers(models.Model):
    name = models.CharField(max_length=30)
    PLATFORM = (("Instagram", "Instagram"), ("TikTok", "TikTok"))
    platform = models.CharField(max_length=15, choices=PLATFORM)
    profile_link = models.URLField(default="https:/instagram.com/ (tiktok.com/@)")
    profile_pic = models.ImageField(null=True, blank=True, default="logo.jpg")
    followersnumber = models.IntegerField()
    phone = models.CharField(max_length=15)


class zayavki(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True, null=True)
