from django.shortcuts import render

from rest_framework.response import Response    
from rest_framework import generics
from rest_framework.views import APIView

from loguru import logger

def HomeView(request):
    return render(request, "work/home.html")

class WorkJournalView(APIView):
    
    def get(self, request):
        
        return Response({
            "data":'data'
        })