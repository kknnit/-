from django.db import models


# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'animals'
        abstract=True


class Dog(Animals):
    age = models.IntegerField(default=8)

    class Meta:
        db_table = 'dog'



class Cat(Animals):
    color=models.CharField(max_length=32)

    class Meta:
        db_table='cat'



class User(models.Model):
    # ImageField这个类型依赖于pillow
    u_icon=models.ImageField(upload_to='icon')

    class Meta:
        db_table='user'



