from . import models
from . import serializers
from rest_framework import viewsets, permissions
from rest_framework import filters

class modelsViewSet(viewsets.ModelViewSet):
    """ViewSet for the models class"""

    queryset = models.models.objects.all()
    serializer_class = serializers.modelsSerializer
    permission_classes = [permissions.IsAuthenticated]


    filter_backends = (filters.SearchFilter,)
    search_fields = ('patient_no', 'patient_name','triage_id')


