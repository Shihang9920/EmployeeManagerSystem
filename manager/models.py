from django.db import models


# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(varbose_name='标题', max_length=32)
