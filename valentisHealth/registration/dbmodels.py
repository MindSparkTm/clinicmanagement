import os, csv
from registration.models import County

path = "/opt/valentisHealth/"

os.chdir(path)

with open('county.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['County'])
        cnty = row['County']
        p = County.objects.create(county_name=cnty)
        p.save()


 path = "/Users/redpulse/Documents/ValentisHealth/valentishealth/valentisHealth"



import os, csv
# from registration.models import InsuranceCompanies

path = "/opt/valentisHealth/"

os.chdir(path)

with open('medicalinsurance.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'])
        p = InsuranceCompanies.objects.create(Name=row['Name'])
        p.save()

