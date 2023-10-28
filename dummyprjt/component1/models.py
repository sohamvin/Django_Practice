from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120) # charfeild must have the max_length atri
    price = models.FloatField(db_index=True, default=2.12345678912345)
    dis = models.TextField(default="abcd")
    #what to do when adding more feilds to a model(Product in this case.)
    #just makemigrations and migrate.
    #but now the new feild will be only present in any models you make after this point.
    #the new feild will not be in the previously created model. so do this->
    abool = models.BooleanField(default = True) #either null = True, or default = True
    #go to 0001_initial.py in migrations. since there is no new filed, when makemigrations, press 1, then migrate



class userData(models.Model):

    email = models.CharField(max_length=130)
    name = models.CharField(max_length=130)
    password = models.CharField(max_length=130)

    def __str__(self):
        global count  # Add this line to indicate you're using the global count variable
        count += 1
        return "userobj" + str(count)


count = 0  # Initialize count variable outside the class