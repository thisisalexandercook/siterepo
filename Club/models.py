from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=50)
    photo = models.ImageField()
    price = models.IntegerField()
    available = models.BooleanField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    Address = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    persons = models.IntegerField()
    child = models.IntegerField()
    a_date = models.CharField(max_length=10)
    d_date = models.CharField(max_length=10)
    email = models.CharField(max_length=50)


class Gallery(models.Model):
    image = models.ImageField()


