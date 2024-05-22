from .models import Therapist
from .serializer import TherapistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SearchForm, TherapistForm

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

def search_therapists(request):
    form = TherapistForm(request.GET or None)
    therapists = []

    if form.is_valid():
        location = form.cleaned_data.get('location')
        therapy_type = form.cleaned_data.get('therapy_type')

        if location or therapy_type:
            query = {}
            if location:
                query['location__iexact'] = location
            if therapy_type:
                query['type_of_therapy__iexact'] = therapy_type
            
            therapists = Therapist.objects.filter(**query)
    
    return render(request, 'find-a-therapist.html', {'form': form, 'therapists': therapists})

# Add a user
@api_view(['POST'])
def addUsers(request):
    serializer = TherapistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def find_a_therapist(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data.get('location')
            therapy_type = form.cleaned_data.get('type_of_therapy')
            therapists = Therapist.objects.all()
            if location:
                therapists = therapists.filter(location__icontains=location)
            if therapy_type:
                therapists = therapists.filter(type_of_therapy__icontains=therapy_type)
            return render(request, 'find-a-therapist.html', {'form': form, 'therapists': therapists})
    else:
        form = SearchForm()
    return render(request, 'find-a-therapist.html', {'form': form})

def therapist_registration(request):
    if request.method == 'POST':
        form = TherapistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TherapistForm()
    return render(request, 'therapists.html', {'form': form})