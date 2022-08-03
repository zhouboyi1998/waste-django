from django.db import models


# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, verbose_name='主键ID')
    category_name = models.CharField(max_length=16, verbose_name='分类名称')
    icon = models.CharField(max_length=255, null=True, verbose_name='分类图标')
    description = models.TextField(verbose_name='分类介绍')
    regulation = models.TextField(verbose_name='投放规定')
    include = models.TextField(verbose_name='主要包括哪些垃圾')
    create_time = models.DateTimeField(verbose_name='创建时间')

    class Meta:
        db_table = 'tb_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name
