from django.db import models

class Post(models.Model):
    title = models.CharField('Name', max_length = 40)
    content = models.TextField('Content', null = True)
    date = models.DateField('Date', null = True)
    topic = models.CharField('Topic', null=True)
    short_info = models.CharField('ShortInfo', null=True)
    banner = models.ImageField(default='photo_test.jpg', blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.id}'
