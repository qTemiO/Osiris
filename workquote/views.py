from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView

from loguru import logger

def HomeView(request):
    return render(request, "work/home.html")