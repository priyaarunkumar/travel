from django.urls import path
from . import views
app_name='arunpriya'
urlpatterns = [



    path('',views.fun,name='fun'),
    path('movie/<int:place_id>/', views.details,name='details'),
    path('add/', views.add,name='add'),
    path('edit/<int:id>/', views.edit, name='edit')
    # path('',views.s,name='s')
]