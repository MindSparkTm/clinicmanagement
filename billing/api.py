from . import models
from . import serializers
from rest_framework import viewsets, permissions, filters

class BillingService(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Billing.objects.all()
    serializer_class = serializers.patientBillSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('service',)




