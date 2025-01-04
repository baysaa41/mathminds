from django.shortcuts import render

# Create your views here.

# accounts/views.py
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

