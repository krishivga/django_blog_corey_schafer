"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importing Admin to get access to admintools URL
from django.contrib import admin

# Importing path for pathing
# Include to include the URLs inside the app URL files
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Tools
    path('', include('basic_blog.urls'))  # Blog URLs
]
