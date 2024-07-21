# Allows us to actually path URLs to views
from django.urls import path
# Importing the views from the same directory to access them for Responses
from . import views


# Where we actually create the URLs
urlpatterns = [
    # The path is empty, which means this is homepage
    path('', views.home, name="blog-home"),
    # views.home is accessing the function we created in views.py
    # We give it a name to make it easier to access later on

    # Creating another page as an about page.
    path('about/', views.about, name="blog-about"),
]
