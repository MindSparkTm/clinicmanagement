import os, csv
path = "C:/Users/hp/Documents/valentishealth/valentisHealth/"

os.chdir(path)
from payments.models import memberinfosanlamdatabase

with open('memberdata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = memberinfosanlamdatabase.objects.create(FAMILY_NO=row['FAMILY_NO'], MEMBER_NO=row['MEMBER_NO'],FIRST_NAME=row['FIRST_NAME'],SURNAME=row['SURNAME'],OTHER_NAMES=row['OTHER_NAMES'],DOB=row['DOB'],USER_ID=row['USER_ID'],CANCELLED=row['CANCELLED'])
        p.save()
