from .models import Therapist
from .serializer import TherapistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
   urls = {
        'All Posts':'posts',
        'View single post':'post/<uuid:id>',
        'Create post':'create-post',
        'Delete post':'delete-post/<uuid:id>',
        'Edit post':'edit-post/<uuid:id>',
    }
   return Response(urls)

# List all users
@api_view(['GET'])
def listUsers(request):
    posts = Therapist.objects.all()
    list = TherapistSerializer(posts,many=True)
    return Response(list.data)

# Add a user
@api_view(['POST'])
def addUsers(request):
    serializer = TherapistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)