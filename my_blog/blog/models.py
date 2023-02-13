from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    datatime = models.DateField(u'Дата публикации')
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id