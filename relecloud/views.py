from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    return render(request, 'index.html')

def sample(request):
    return render(request, 'index.html')

def data(request):
    return HttpResponse({"hello": "hai"})

class DestinationViewSet(ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def list(self, request, *args, **kwargs):
        logger.info("GET request for Destination view")
        return super().list(request, *args, **kwargs)
    
    def create(self, request):
        logger.info("POST request for Destination view")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Record successfully created")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error(f"POST request validation errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
