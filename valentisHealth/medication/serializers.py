from . import models

from rest_framework import serializers


class modelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.models
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'prescription_id', 
            'patient_no', 
            'patient_name', 
            'address', 
            'phone_number', 
            'signature', 
            'prescription', 
        )

class mydawaserializer(serializers.ModelSerializer):

    class Meta:
        model = models.MyDawa
        fields = (
            'brand',
            'size',
            'price',


        )

class mydawaprescriptions(serializers.ModelSerializer):
    class Meta:
        model = models.models
        fields = (
            'prescription',
            'created',
        )