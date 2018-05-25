from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# from blog.forms import FileUploadForm
# from blog.forms import stt

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    return render(request,'blog/home.html',{})

def realtime(request):
    return render(request, 'blog/r.translate.html', {})

def audio_translate(request):
    return render(request, 'blog/a.translate.html',{})
