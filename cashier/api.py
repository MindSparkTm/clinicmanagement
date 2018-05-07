from . import models
from . import serializers
from rest_framework import viewsets, permissions, filters

class Cashierservice(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.PatientBill.objects.all()
    serializer_class = serializers.totalBillSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('patientid','invoiceid',)







