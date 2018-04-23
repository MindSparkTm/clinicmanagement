from . import models

from rest_framework import serializers


class modelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Medication
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'prescription_id',
            'patient_no',
            'patient_name', 
            'address', 
            'phone_number',
            'pharmacy',
            'signature', 
            'prescription',
            'email'
        )

class mydawaserializer(serializers.ModelSerializer):

    class Meta:
        model = models.MyDawa
        fields = (
            'brand',
            'size',
            'price',


        )

