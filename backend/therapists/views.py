from .models import Therapist
from .serializer import TherapistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
