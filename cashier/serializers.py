from . import models

from rest_framework import serializers


class totalBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PatientBill
        fields = '__all__'




