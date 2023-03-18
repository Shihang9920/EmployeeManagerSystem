"""EmployeeManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import manager.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', manager.views.departlist),
    path('depart/add/', manager.views.adddepart),
    path('depart/delete/', manager.views.departdelete),
    path('depart/<int:nid>/edit/', manager.views.departedit),
    path('', manager.views.index),
    path('login/', manager.views.login),
    path('user/list/', manager.views.userlist),
    path('user/add/', manager.views.adduser),
    path('user/<int:nid>/edit/', manager.views.useredit),
    path('user/delete/', manager.views.userdelete),
    path('project/list/', manager.views.projectlist),
    path('project/add/', manager.views.projectadd),
]
