from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Therapist
from .serializer import TherapistSerializer

class TherapistList(APIView):
    def get(self, request):
        therapists = Therapist.objects.all()
        serializer = TherapistSerializer(therapists, many=True)
        return Response(serializer.data)

class TherapistDetail(APIView):
    def get(self, request, pk):
        therapist = Therapist.objects.get(pk=pk)
        serializer = TherapistSerializer(therapist)
        return Response(serializer.data)
