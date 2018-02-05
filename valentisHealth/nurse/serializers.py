from . import models

from rest_framework import serializers


class modelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.models
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'systolic', 
            'diastolic', 
            'temperature', 
            'oxygen_saturation', 
            'urinalysis', 
            'heart_rate', 
            'others', 
            'attending_nurse', 
            'patient_no', 
            'first_name', 
            'last_name', 
            'middle_name', 
        )


