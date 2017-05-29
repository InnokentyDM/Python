from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings

from .forms import PostForm
from .models import Post


def landing(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()

    return render(request, 'landing/landing.html', locals())


def posts(request):
    post_list = Post.objects.all()
    return render_to_response('landing/posts.html', {'post_list': post_list})