from django.db import models

# Create your models here.



class PatientBill(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    patientid = models.CharField(max_length=255,blank=True)
    totalbill = models.CharField(max_length=500,blank=True)
    billbreakdown = models.CharField(max_length=500,blank=True)
    invoiceid = models.CharField(max_length=500,blank=True)


