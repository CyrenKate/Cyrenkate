from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.mainpage, name="mainpage"),
    path('commission/', views.Commissioning, name="commission"),
    path('basic_info/', views.clientInfo, name="basic_info"),
    path('delete_basic_info/<int:biid>/',views.Delete_BasicInfo, name = "delete_basic_info"),
    path('edit_basic/<int:biid>/',views.edit, name = "edit_basic"),
    path('update_basic/<int:biid>/',views.update, name = "update_basic"),
    path('authorinfo/', views.authorInfo, name="authorinfo"),
    path('artstyle/', views.porartstyle, name="artstyle"),
    path('comstwo/', views.comsTwo, name="comstwo"),
]