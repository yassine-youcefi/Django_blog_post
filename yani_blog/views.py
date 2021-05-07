from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,User





def index(request):

    posts = Post.objects.all()
    print('this is my posts >> \n',posts)
    context={
        'posts' : posts,
        'title' : 'Home page'

    }
    return render(request, 'templates/index.html', context)

 
def about(request):
    return render(request, 'templates/about.html')
 