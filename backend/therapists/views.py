from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Therapist
from .serializer import TherapistSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Therapist.objects.all()
    serializer_class =  TherapistSerializer