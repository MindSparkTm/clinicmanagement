import os, csv

path = "C:\\Users\\hp\\Documents\\valentishealth\\valentisHealth\\registration"

os.chdir(path)
from registration.models import MedicationHistory

with open('familyhistory.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = MedicationHistory.objects.create(Disease=row['Disease'])
        p.save()