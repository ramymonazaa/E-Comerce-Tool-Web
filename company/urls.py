"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from turtle import home
from urllib import request
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from company import views
from app1 import views as v_app
from app1.models import tool
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("app1.urls")),
    url(r'^admin/', admin.site.urls), 
    url(r'^$',views.homepage),
    path('home',views.homepage , name='home'),
    path('insert',v_app.insert_tool , name='insert'),
    path('show_tool',v_app.show_tool , name='show_tool'),
    path('<int:id>',v_app.insert_cart , name='insert_cart1'),
    path('index <int:id_>',v_app.category1 , name='category'),
]
urlpatterns+=staticfiles_urlpatterns()#sypport take urls from html