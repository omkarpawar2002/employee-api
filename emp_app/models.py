from django.db import models


# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dept = models.CharField(max_length=100)
    sal = models.FloatField()