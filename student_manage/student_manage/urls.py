"""student_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import () function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin

from .import views



urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('base/',views.BASE,name='base'),
    re_path('studentdetails/',views.STUDENTDETAILS,name='studentdetails'),
    re_path('adddata/',views.adddata,name='adddata'),
    re_path('add/',views.ADD,name='add'),
    re_path('remove/',views.REMOVE,name='remove'),
    re_path('marks/',views.MARKS,name='marks'),
]