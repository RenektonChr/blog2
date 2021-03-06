#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blogs/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})
