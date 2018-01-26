from . import models

from rest_framework import serializers


class modelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.models
        fields = (
            'pk', 
            'patient_id', 
            'created', 
            'last_updated', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'Gender', 
            'street_name', 
            'apartment_name', 
            'postal_code', 
            'postal_address', 
            'city', 
            'country', 
            'age', 
            'next_of_kin', 
            'n_of_kin_rel', 
            'email', 
            'phone', 
            'primary_insurance', 
            'secondary_insurance', 
            'pri_ins_sub', 
            'sec_ins_sub', 
            'other_ins_subscriber', 
            'subscriber_relationship', 
            'sub_address', 
            'ss_number', 
            'sub_ss_number', 
            'alt_phone', 
            'sub_work_phone', 
            'dob', 
            'sub_dob', 
            'sub_employer', 
        )


