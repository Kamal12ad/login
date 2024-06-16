from django.db import models

# Create your models here.

# class userInfo(models.Model):
#     Username = models.CharField(max_length=50)
#     Email = models.CharField(max_length=50)
#     Password = models.CharField(max_length=50)


class usertable(models.Model):
     Username = models.CharField(max_length=50)
     Email = models.CharField(max_length=50)
     Password = models.CharField(max_length=50)
