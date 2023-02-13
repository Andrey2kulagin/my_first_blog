from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    datatime = models.DateField(u'Дата публикации')
    content = models.TextField(max_length=10000)
