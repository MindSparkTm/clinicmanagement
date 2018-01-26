from . import models

from rest_framework import serializers


class pre_authSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.pre_auth
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'reference_no', 
            'authority_type', 
            'provider', 
            'ward', 
            'date_admitted', 
            'date_provided', 
            'notes', 
            'claim', 
            'limit', 
            'batch_no', 
            'date_reported', 
            'admit_days', 
            'anniv', 
            'daily_bed_limit', 
            'type', 
            'authorised_by', 
        )


