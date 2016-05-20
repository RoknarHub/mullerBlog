from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

class BlogEntry(models.Model):
    blog_title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    blog_content = models.TextField()
    blog_description = models.CharField(max_length=200)
    blog_thumbnail = models.URLField(max_length=200)

    def __str__(self):
        return self.blog_title

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin.order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'