from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('user/',views.listUsers,name='posts'),
    path('user/create/',views.addUsers,name='create-post'),
]
