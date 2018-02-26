import os, csv

path = "C:\\Users\\hp\\Documents\\valentishealth\\valentisHealth\\registration"

os.chdir(path)
from registration.models import InsuranceCompanies

with open('medicalinsurance.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = InsuranceCompanies.objects.create(Name=row['Name'])
        p.save()