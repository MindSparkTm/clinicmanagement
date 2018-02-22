import os, csv

path = "C:\\Backup_Valentis\\valentishealth\\valentisHealth"
os.chdir(path)
from registration.models import County

with open('county.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = County.objects.create(County=row['County'])
        p.save()
