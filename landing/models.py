import os

from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


class Post(models.Model):
    image = models.ImageField()
    comment = models.CharField(max_length=255)

    def url(self):
        return str(self.image.url)

    def admin_thumbnails(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))
    admin_thumbnails.allow_tags = True