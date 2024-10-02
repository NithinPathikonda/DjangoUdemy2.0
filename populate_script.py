import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
 
import django
django.setup()
 
import random 
from first_app.models import Data
from faker import Faker
 
fakegen=Faker()

 
def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
 
         #creating the fake data for the entry 
        first_name=fakegen.name()
        last_name=fakegen.name()
        email=fakegen.email()

        data_add=Data.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        data_add.save()

 
if __name__ == '__main__':
    print('Populating Script!!')
    populate(20)
    print('Populating Complete')