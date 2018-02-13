from . import models

from rest_framework import serializers


class patientVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.patientVisit
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'patient_no', 
            'visit_id', 
            'radiology_no', 
            'notes', 
            'diagnosis', 
            'prescription_id', 
            'status',
            'triage_id'
        )


class DiagnosisSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Diagnosis
        fields = (
            'code',
            'name',
        )

