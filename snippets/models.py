from django.db import models

# Create your models here.
#  emloyyes taple : name, checkin time , checkout time

class Employyes(models.Model):
    name = models.CharField(max_length=100)
    checkIn = models.DateTimeField(auto_now_add=True)
    checkOut = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

#  diabetes taple : glocos, bmi, prusser

class Diabetes(models.Model):
    glocos = models.FloatField(max_length=10)
    bmi = models.FloatField(max_length=10)
    prusser = models.FloatField(max_length=10)

    def __str__(self):
        return self.glocos

#  clothes taple : name, price, description

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    description = models.TextField()
    def __str__(self):
        return self.name
