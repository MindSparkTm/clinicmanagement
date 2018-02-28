import os, csv
from registation.models import County

path = "/opt/valentisHealth/"

# path= os.path.abspath(os.path.realpath(path))
#
# os.chdir(path)

with open('/opt/valentisHealth/county.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['County'])
        p = County.objects.create(county_name=row['County'])
        p.save()
