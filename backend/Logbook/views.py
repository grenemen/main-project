from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import BernLogSerializer
from .models import BernLog, MarlyLog

class BernLogView(viewsets.ModelViewSet):
    serializer_class = BernLogSerializer
    queryset = BernLog.objects.all()

class MarlyLogView(viewsets.ModelViewSet):
    serializer_class = BernLogSerializer
    queryset = MarlyLog.objects.all()