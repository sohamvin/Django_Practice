"""
URL configuration for dummyprjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from component1 import views
from django.urls import include

urlpatterns = [

    path('', views.Home, name = 'home'),
   # path('home/', views.Home, name = 'apath1'),
    path('About/', views.About, name = 'apath2'),
    path('Link/', views.Link, name = 'apath3'),
    path('to/', views.fn_without_req, name = 'apth4'),
    path('areq/', views.another, name = 'path5'),
    path('home/', views.home, name = 'path5'),
    path('about/', views.about, name = 'path6'),
    path('services/', views.services, name = 'path7'),
    path('contacts/', views.contacts, name = 'path8'),
    path('form/', views.create_user, name = 'path9'),
    path('printer/', views.display_product_detail, name = 'path10'),
    path('login/', views.check, name = 'path11'),
]
