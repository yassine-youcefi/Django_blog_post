from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,User
from django.views.generic import ListView



def index(request):
    context={
        'posts' : Post.objects.all(),
        'title' : 'Home page'

    }
    return render(request, 'templates/index.html', context)

class PostListView():
    model = Post 

 
def about(request):
    return render(request, 'templates/about.html')
 