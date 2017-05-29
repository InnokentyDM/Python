from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static

from . import views

urlpatterns = [
    url(r'^landing/', views.landing, name='landing'),
    url(r'^posts/', views.posts, name='posts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
