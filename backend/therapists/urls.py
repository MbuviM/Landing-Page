from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from therapists import views

urlpatterns = [
    path("therapists/", views.SnippetList.as_view()),
    path("therapists/<int:pk>/", views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)