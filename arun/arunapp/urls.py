
from django.urls import path,include
from . import views
urlpatterns = [

    path('r',views.regi,name='regi'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout')
    ]