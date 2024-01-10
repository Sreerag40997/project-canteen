"""
URL configuration for untitled1 project.

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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from myapp import views

urlpatterns = (
    path('login/', views.login),
    path('login_post/',views.login_post),
    path('addfoods/', views.addfoods),
    path('addfood_post/',views.addfood_post),
    path('addstaffs/',views.addstaffs),
    path('addstaff_post/',views.addstaff_post),
    path('addtodaymenus/',views.addtodaymenus),
    path('addtodaymenu_post/',views.addtodaymenu_post),
    path('addusers/',views.addusers),
    path('addusers_post/',views.addusers_post),
    path('viewsprecount/',views.viewsprecount),
    path('billviews/',views.billviews),
    path('foodviews/',views.foodviews),
    path('orderhistoryviews/',views.orderhistoryviews),
    path('orderhistoryviews_post/',views.orderhistoryviews_post),
    path('staffviews/',views.staffviews),
    path('staffviews_post/',views.staffviews_post),
    path('todaymenueviews/',views.todaymenueviews),
    path('todaymenueviews_post/',views.todaymenueviews_post),
    path('delete_todaysmenu/<id>',views.delete_todaysmenu),
    path('usersview/',views.usersview),
    path('usersview_post/',views.usersview_post),
    path('adminhomes/',views.adminhomes),
        path('changepassword_post/',views.changepasswords_post),
    path('changepassword/',views.changepassword),
    path('viewordermore/<id>',views.viewordermore),
    path('indexs/',views.index),
    path('editfood/<did>',views.editfood),
    path('editfood_POST/',views.editfood_post),
    path('deletefood/<id>',views.deletefood),
    path('editstaff/<id>',views.editstaffs),
    path('editstaff_POST/',views.editstaffs),



)
