# django.shortcuts render allows us to use a faster way to render HTML content
from django.shortcuts import render

# Allows us to send out HTTPResponses
from django.http import HttpResponse

from .models import Post


posts = [
    {
        'author': 'KrishivGA',
        'title': 'Blog Post 1',
        'content': 'Hello world! New Blogpost!',
        'date posted': "22nd July, 2024"
    },
    {
        'author': 'MartinSM',
        'title': 'Blog Post 2',
        'content': 'Good evening! New Blogpost!',
        'date_posted': '1st December, 2024'

    }
]

# Creating a view function that will let us view the `/home` page


def home(request):
    # We take a request from the user (which is given through urls.)
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "basic_blog/home.html", context)
    # We return some basic HTML as a response


def about(request):
    # Creating another page called about
    return render(request, "basic_blog/about.html", {'title': 'About'})
