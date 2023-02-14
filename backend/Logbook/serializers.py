# Responsible to convert the model instances to JSON, so frontend can work with the received data

from rest_framework import serializers
from .models import BernLog, MarlyLog

class BernLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BernLog
        fields = '__all__'

class MarlyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarlyLog
        fields = '__all__'



