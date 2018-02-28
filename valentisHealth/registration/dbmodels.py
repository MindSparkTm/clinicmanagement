import os, csv
from registration.models import County

path = "/opt/valentisHealth/"

os.chdir(path)

with open('county.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['County'])
        cnty = row['County']
        p = County.objects.create(County=cnty)
        p.save()

path = "/Users/redpulse/Documents/ValentisHealth/valentishealth/valentisHealth"

import os, csv

# from registration.models import InsuranceCompanies

path = "/opt/valentisHealth/"

os.chdir(path)

with open('Allergies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['allergy_name'])
        p = Allergies.objects.create(allergy_name=row['allergy_name'])
        p.save()


path = "/opt/valentisHealth/"
os.chdir(path)

with open('Allergies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = County.objects.create(allergy_name=row['allergy_name'])
        p.save()

