from .models import Therapist
from .serializer import TherapistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SearchForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .models import User
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def find_a_therapist(request):
    model = Therapist
    return render(request, 'find-a-therapist.html')

def therapist_registration(request):
    model = Therapist
    return render(request, 'therapists.html')

def success(request):
    return render(request, 'success.html')

def search_therapists(request):
    model = Therapist
    return render(request, 'search-therapists.html')

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

# Add a user
@api_view(['POST'])
def addUsers(request):
    serializer = TherapistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Register a therapist
@csrf_protect

def therapist_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        type_of_therapy = request.POST.get('type_of_therapy')
        years_of_experience = request.POST.get('years_of_experience')
        image = request.FILES.get('image')
        fee_per_session = request.POST.get('fee_per_session')
        monthly_slots = request.POST.get('monthly_slots')
        monthly_fee = request.POST.get('monthly_fee')
        accepts_queer_clients = request.POST.get('accepts_queer_clients') == 'on'

        therapist = Therapist(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            location=location,
            gender=gender,
            age=age,
            type_of_therapy=type_of_therapy,
            years_of_experience=years_of_experience,
            image=image,
            fee_per_session=fee_per_session,
            accepts_queer_clients=accepts_queer_clients
        )
        therapist.save()
        return redirect('success')  # Replace with your success page URL

    return render(request, 'therapists.html')

   
# Sessions
def index(request):
    
    num_therapists = Therapist.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_therapists': num_therapists,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

# Multi Role Authentication

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers) 
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Successfully logged out.'})

