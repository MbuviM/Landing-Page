from django.urls import path
from .views import TherapistList, TherapistDetail

urlpatterns = [
    path('therapists/', TherapistList.as_view()),
    path('therapists/<int:pk>/', TherapistDetail.as_view()),
]
