from django.db import models

# Create your models here.
from datetime import datetime


class Upload(models.Model):
    '''上传文件使用的映射类
    '''

    # 访问页面的次数
    downloadcount = models.IntegerField(verbose_name='访问次数', default=0)
    # 该字段作为一个文件的唯一标识
    code = models.CharField(verbose_name='code', max_length=8)
    # 文件上传时间
    datetime = models.DateTimeField(verbose_name='上传时间',
                                    default=datetime.now())
    # 文件存储路径
    path = models.CharField(verbose_name='存储路径', max_length=64)
    # 文件名
    name = models.CharField(verbose_name='文件名', max_length=32)
    # 文件大小
    filesize = models.CharField(verbose_name='文件大小', max_length=8)
    # 上传文件的客户端的 IP 地址
    pcip = models.CharField(verbose_name='IP 地址', max_length=16)

    # 这个方法用于格式化类的实例的打印样式，便于测试
    def __str__(self):
        return self.name
