from django.db import models


# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32)


class Employees(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    gender_choice = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(choices=gender_choice)
    age = models.IntegerField
    depart = models.ForeignKey(to="Department", to_field='id', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField()
