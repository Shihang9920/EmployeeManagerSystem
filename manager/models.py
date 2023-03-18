from django.db import models


# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Employees(models.Model):
    name = models.CharField(max_length=16, verbose_name="姓名")
    password = models.CharField(max_length=64, verbose_name="密码")
    gender_choice = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(choices=gender_choice, verbose_name="性别")
    depart = models.ForeignKey(to="Department", to_field='id', on_delete=models.CASCADE, verbose_name="部门")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="余额")
    create_time = models.DateField(verbose_name="入职时间")


class Project(models.Model):
    name = models.CharField(max_length=16, verbose_name='名称')
    Funds = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='投资')
    level_choice = ((1, '普通'), (2, '高级'), (3, '顶级'))
    level = models.SmallIntegerField(choices=level_choice, verbose_name='级别')
    status_choice = ((1, '进行中'), (2, '已交付'))
    status = models.SmallIntegerField(choices=status_choice,verbose_name='状态')