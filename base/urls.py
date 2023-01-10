from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.hom,name="hom"),
    path('room/<str:pk>/',views.room,name="room"),                     #'<str:pk>' gives dynamic change in url(enter in specific path)...it may be num,str or slug
    path('create_room/',views.createroom,name="create_room"),
    path('update_room/<str:pk>/',views.updateroom,name="update_room"),
    path('delroom/<str:pk>/',views.delroom,name="delroom"),
    ]
