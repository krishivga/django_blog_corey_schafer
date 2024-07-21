# django.shortcuts render allows us to use a faster way to render HTML content
from django.shortcuts import render

# Allows us to send out HTTPResponses
from django.http import HttpResponse


# Creating a view function that will let us view the `/home` page
def home(request):  # We take a request from the user (which is given through urls.)
    return HttpResponse("<h1>Blog Home</h1>")
    # We return some basic HTML as a response


def about(request):
    # Creating another page called about
    return HttpResponse("<h1>Blog About</h1>")
