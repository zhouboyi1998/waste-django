from django.db import models


# Create your models here.

class Waste(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, verbose_name='主键ID')
    waste_name = models.CharField(max_length=32, verbose_name='垃圾名称')
    image = models.CharField(max_length=255, null=True, verbose_name='垃圾图片')
    classification_id = models.IntegerField(verbose_name='分类ID')
    create_time = models.DateTimeField(verbose_name='创建时间')

    class Meta:
        db_table = 'tb_waste'
        verbose_name = '垃圾'
        verbose_name_plural = verbose_name
