from .models import Therapist
from .serializer import TherapistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def find_a_therapist(request):
    return render(request, 'find-a-therapist.html')

def therapist_registration(request):
    return render(request, 'therapists.html')

# Create your views here.
@api_view(['GET'])
def index(request):
    urls = {
        'All Posts': 'posts',
        'View single post': 'post/<uuid:id>',
        'Create post': 'create-post',
        'Delete post': 'delete-post/<uuid:id>',
        'Edit post': 'edit-post/<uuid:id>',
    }
    return Response(urls)

def index(request):
    location = request.GET.get('location')
    type_of_therapy = request.GET.get('type_of_therapy')

    therapists = Therapist.objects.all()
    if location:
        therapists = therapists.filter(location__icontains=location)
    if type_of_therapy:
        therapists = therapists.filter(type_of_therapy__icontains=type_of_therapy)

    context = {
        "therapists": therapists,
    }
    return render(request, "find-a-therapist.html", context)


# Get a therapist
@api_view(['GET'])
def search_therapists(request):
    location = request.GET.get('location')
    type_of_therapy = request.GET.get('type_of_therapy')

    # Filter therapists based on query parameters
    therapists = Therapist.objects.all()
    if location:
        therapists = therapists.filter(location__icontains=location)
    if type_of_therapy:
        therapists = therapists.filter(type_of_therapy__icontains=type_of_therapy)

    serializer = TherapistSerializer(therapists, many=True)
    return Response(serializer.data)

# Add a user
@api_view(['POST'])
def addUsers(request):
    serializer = TherapistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
