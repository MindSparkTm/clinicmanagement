import os, csv

path = "/opt/valentisHealth"

os.chdir(path)
from clinic.models import Radiologylist

with open('radiology.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = Radiologylist.objects.create(group=row['Group'],modality=row['Modality'],tests=row['Tests'])
        p.save()
