from django.db import models


class Articles(models.Model):
    title = models.CharField('name', max_length=50)
    announce = models.CharField('announce', max_length=250)
    full_text = models.TextField('article')
    date = models.DateTimeField('date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'