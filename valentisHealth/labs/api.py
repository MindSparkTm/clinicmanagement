from . import models
from . import serializers
from rest_framework import viewsets, permissions


class labsViewSet(viewsets.ModelViewSet):
    """ViewSet for the labs class"""

    queryset = models.labs.objects.all()
    serializer_class = serializers.labsSerializer
    permission_classes = [permissions.IsAuthenticated]


class radiologyViewSet(viewsets.ModelViewSet):
    """ViewSet for the radiology class"""

    queryset = models.radiology.objects.all()
    serializer_class = serializers.radiologySerializer
    permission_classes = [permissions.IsAuthenticated]


