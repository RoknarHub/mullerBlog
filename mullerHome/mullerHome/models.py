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
    is_preview = models.BooleanField(default=True)

    def __str__(self):
        return self.blog_title

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def blog_entry_is_released(self):
        return not self.is_preview
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Released?'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blogEntry', args=[str(self.id)])