from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,User





def index(request):
    context={
        'posts' : Post.objects.all(),
        'title' : 'Home page'

    }
    return render(request, 'templates/index.html', context)

 
def about(request):
    return render(request, 'templates/about.html')
 