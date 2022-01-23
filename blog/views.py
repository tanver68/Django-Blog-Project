from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Tanver',
        'title' : 'Blog Post',
        'content' : 'dhgfhg',
        'date_posted' : 'January 23,2022' 
    },
     {
        'author' : 'Rabby',
        'title' : 'Blog Post',
        'content' : 'gjh',
        'date_posted' : 'January 24,2022' 
    }
]

def home (request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html',{'title':'About'})
