from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('templates/libros/', views.blogsingle, name='blogsingle'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]