from django.db import models

# Create your models here.



class Billing(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    service = models.CharField(max_length=255,blank=True)
    price = models.CharField(max_length=500,blank=True)

