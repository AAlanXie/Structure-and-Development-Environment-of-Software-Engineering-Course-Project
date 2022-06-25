from django.db import models

# Create your models here.
class Information(models.Model):
    #姓名
    username = models.CharField(primary_key = True, max_length = 20)
    #密码
    password = models.CharField(max_length = 20)


    def __str__(self):
        return self.username

class Event(models.Model):
    #事件名称
    event_name = models.TextField()
    #事件经度
    event_longitude = models.FloatField()
    #事件纬度
    event_latitude = models.FloatField()
    #事件描述
    event_describe = models.TextField()

    def __str__(self):
        return self.event_name