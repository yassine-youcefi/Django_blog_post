from django.shortcuts import render
from django.http import HttpResponse
from .models import User

posts = [

    {
        'author': 'yassine youcefi',
        'title': 'Blog jdid hada 1',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 21'
    },
    {
        'author': 'chaindraa wahid',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 22'

    },
    {
        'author': 'habibi fouad',
        'title': 'Blog for fouad 2',
        'content': ' first blog for test fouad it is hardcoded',
        'date_posted': 'Mai 30'

    },
    {
        'author': 'ghazali fatima',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 29'

    },
    {
        'author': 'chaindraa wahid',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 22'

    },
    {
        'author': 'yassine youcefi',
        'title': 'Blog jdid hada 1',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 21'
    },
    {
        'author': 'chaindraa wahid',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 22'

    },
    {
        'author': 'habibi fouad',
        'title': 'Blog for fouad 2',
        'content': ' first blog for test fouad it is hardcoded',
        'date_posted': 'Mai 30'

    },
    {
        'author': 'ghazali fatima',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 29'

    },
    {
        'author': 'chaindraa wahid',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 22'

    }
]



def index(request):
    context={
        'posts' : posts,
        'title' : 'Home page'

    }
    return render(request, 'templates/index.html', context)

 
def about(request):
    return render(request, 'templates/about.html')
 