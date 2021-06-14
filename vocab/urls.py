from django.urls import path
from . import views
from django.conf import settings

appname= 'vocab'

urlpatterns = [

    path('',views.index,name= 'index'),
    path('add/', views.wordin, name = 'add'),
    path('list/', views.wordshow, name = 'show'),
]