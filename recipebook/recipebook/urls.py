"""
URL configuration for recipebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from core.views import login, register, listing, recipe, recipeedit, recipelist

urlpatterns = [
    path("",login,name='login'),
    path('register/', register, name='register'),
    path('listing/', listing, name='listing'),
    path('recipe/', recipe, name='recipe'),
    path('recipeedit/', recipeedit, name='recipeedit'),
    path('recipelist/', recipelist, name='recipelist'),
    
    path('admin/', admin.site.urls),
]
