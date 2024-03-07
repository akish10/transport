"""from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Register(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_name = models.CharField(max_length=25, unique=True)
    email= models.EmailField()

    password=models.CharField(max_length=32)



    def set_password(self,raw_password):

       self.password = make_password(raw_password)

    def check_password(self, raw_password):

        return check_password(raw_password, self.password)




 
class Vehicle(models.Model):

    Vehicle_id = models.CharField(max_length=8, unique=True)
    Capacity = models.IntegerField()
    Type = models.CharField(max_length=20)
    refrigerated = models.BooleanField()
    

    #def __str__(self):
        #return self.unique_number



class Product(models.Model):

    product_name = models.CharField(max_length=30)
    select_type = {'Perishable':'Easily goes bad',
    'Non Perishable': 'Stays for long',} 
    Type = models.CharField(max_length=14,choices=select_type)


class Route(models.Model):

    start_location = models.CharField(max_length=25)
    destination = models.CharField(max_length = 25)

class Login(models.Model):

    user_name = models.CharField(max_length=25, unique=True)

    password=models.CharField(max_length=130)


    related_model= models.OneToOneField(Register, on_delete = models.CASCADE)"""


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicle(models.Model):

    Vehicle_id = models.CharField(max_length=8, unique=True)
    Capacity = models.IntegerField()
    Type = models.CharField(max_length=20)
    refrigerated = models.BooleanField()



class Payment(models.Model):
    cardholder = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()
    cvc = models.CharField(max_length=3)
    Vehicle_id = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default=user.id)  

    def __str__(self):
        return f"Payment for Vehicle {self.Vehicle_id} - ${self.amount}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_returned = models.BooleanField(default=False)


class Book(models.Model):
    product = models.CharField(max_length=100)
    perishable = models.BooleanField(default=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    pickup = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
   
    