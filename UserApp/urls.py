from django.urls import path
from UserApp import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('regester/', views.regesterview, name='regester')
]
