"""
URL configuration for movieapiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app.views import Allmovies,Addmovie,Updatamovie,Deletemovie
from app import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.apioverview),
    path('Allmovies/',Allmovies.as_view(),name='Allmovies'),
    path('Addmovie/',Addmovie.as_view(),name='Addmovie'),
    path('Updatamovie/update/<int:pk>/',Updatamovie.as_view(),name='Updatamovie'),
    path('Deletemovie/delete/<int:pk>/',Deletemovie.as_view(),name='Deletemovie'),
    path('serchbycategory/',views.serchbycategory,name='serchbycategory')
]
