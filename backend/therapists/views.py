from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Therapist, User
from .serializer import TherapistSerializer, UserSerializer
from .forms import CreateUserForm, LoginForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def find_a_therapist(request):
    return render(request, 'find-a-therapist.html')

def therapist_registration(request):
    return render(request, 'therapists.html')

def success(request):
    return render(request, 'success.html')

def search_therapists(request):
    return render(request, 'search-therapists.html')

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

@api_view(['POST'])
def addUsers(request):
    serializer = TherapistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_protect
def therapist_register(request):
    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'address': request.POST.get('address'),
            'location': request.POST.get('location'),
            'gender': request.POST.get('gender'),
            'age': request.POST.get('age'),
            'type_of_therapy': request.POST.get('type_of_therapy'),
            'years_of_experience': request.POST.get('years_of_experience'),
            'image': request.FILES.get('image'),
            'fee_per_session': request.POST.get('fee_per_session'),
            'accepts_queer_clients': request.POST.get('accepts_queer_clients') == 'on'
        }
        therapist = Therapist(**data)
        therapist.save()
        return redirect('success')

    return render(request, 'therapists.html')

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response({'detail': 'Successfully logged out.'})
