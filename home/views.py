from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import PostMod


def index(request):
    posts = PostMod.objects.all().values().order_by('-time')
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    x = request.POST['name']
    y = request.POST['content']
    d = y.split()
    post = PostMod(name=x, content=y)
    #Getting strick to offence....
    post.save()
    return HttpResponseRedirect(reverse('index'))

# Create your views here.
