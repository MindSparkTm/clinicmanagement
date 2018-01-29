from . import models
from . import serializers
from rest_framework import viewsets, permissions


class patientVisitViewSet(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.patientVisit.objects.all()
    serializer_class = serializers.patientVisitSerializer
    permission_classes = [permissions.IsAuthenticated]


