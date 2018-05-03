from . import models

from rest_framework import serializers


class patientBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Billing
        fields = '__all__'




