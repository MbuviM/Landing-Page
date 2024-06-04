from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('search/', views.search_therapists, name='search-therapists'),
    path('user/create/',views.addUsers,name='create-post'),
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='password_reset'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('find-a-therapist/', views.find_a_therapist, name='find_a_therapist'),
    path('therapists/', views.therapist_registration, name='therapists'),
    path('therapists/register/success/', views.success, name='success'),
    path('therapists/register/', views.therapist_register, name='therapist_register'),
    path('search therapists/', views.search_therapists, name='search_therapists'),
]

