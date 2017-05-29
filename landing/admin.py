from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "comment", "admin_thumbnails"]



    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)