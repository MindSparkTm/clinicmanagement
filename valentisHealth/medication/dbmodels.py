import os, csv

path = "/Users/redpulse/Documents/ValentisHealth/valentisHealth/valentisHealth/medication/mydawa.csv"
path= os.path.dirname(os.path.realpath(path))
os.chdir(path)
from medication.models import MyDawa

with open('mydawa.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = MyDawa.objects.create(brand=row['brand'], size=row['size'], price=row['price'])
        p.save()
