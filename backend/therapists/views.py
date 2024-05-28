from .models import Therapist
from .serializer import TherapistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SearchForm, TherapistForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, TemplateView
from django.db.models import Q

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
            monthly_slots=monthly_slots,
            monthly_fee=monthly_fee,
            accepts_queer_clients=accepts_queer_clients
        )
        therapist.save()
        return redirect('success')  # Replace with your success page URL

    return render(request, 'therapists.html')

# List Therapist
class TherapistList(ListView):
    model = Therapist
    template_name = 'templates/find-a-therapist.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Therapist.objects.filter(
            Q(location__icontains=query) | Q(type_of_therapy__icontains=query)
        )
        return object_list
