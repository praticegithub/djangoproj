from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class Topic(models.Model):
     name=models.CharField(max_length=150)

     def __str__(self):
         return self.name

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=220)
    desc=models.TextField(null=True,blank=True)
    #parti=
    updated=models.DateTimeField(auto_now=True)
    crated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-updated"]    #this change the order of the lastest entered value

    def __str__(self):
         return self.name

class mssg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True) 
    room=models.ForeignKey(Room,on_delete=models.CASCADE, null=True)
    body=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    crated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
