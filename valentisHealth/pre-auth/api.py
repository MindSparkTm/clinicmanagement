from . import models
from . import serializers
from rest_framework import viewsets, permissions


class pre_authViewSet(viewsets.ModelViewSet):
    """ViewSet for the pre_auth class"""

    queryset = models.pre_auth.objects.all()
    serializer_class = serializers.pre_authSerializer
    permission_classes = [permissions.IsAuthenticated]


