from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.search_therapists, name='search-therapists'),
    path('user/create/',views.addUsers,name='create-post'),
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('find-a-therapist/', views.find_a_therapist, name='find_a_therapist'),
    path('therapists/', views.therapist_registration, name='therapists'),
    path('therapists/register/success/', views.success, name='success'),
    path('therapists/register/', views.therapist_register, name='therapist_register'),
    path('search therapists/', views.search_therapists, name='search_therapists'),

]

