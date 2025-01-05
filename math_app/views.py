from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Problems
from .serializers import ProblemSerializer

class ProblemList(generics.ListCreateAPIView):
    queryset = Problems.objects.filter(pk__lt=10)
    serializer_class = ProblemSerializer