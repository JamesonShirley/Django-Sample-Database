from django.db import models

from datetime import date
# Create your models here.

class Agent(models.Model):
    fName = models.CharField(default = "NA", max_length = 200)
    lName = models.CharField(default = "NA", max_length = 200)
    
    def __str__(self):
        return f"{self.fName} {self.lName}"

class Customer(models.Model):
    fName = models.CharField(default = "NA", max_length = 200)
    lName = models.CharField(default = "NA", max_length = 200)
    age = models.IntegerField(default = 0)
    emailAddress = models.CharField(default = 'NA', max_length = 200)
    agentID = models.ForeignKey(Agent, on_delete=models.CASCADE)
    dateAquired = models.DateField(default = date.today())
    dateLastOrder = models.DateField(default = date.today())
    outstandingOrder = models.CharField(default = "No", max_length = 5)
    dateOfBirth = models.DateField(default = date.today())

    def __str__(self):
        return f"{self.fName} {self.lName}"


class Order(models.Model):
    Product = models.CharField(default = "NA", max_length = 200)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderDate = models.DateField(default = date.today())
    EstimatedDelivery = models.DateField(default = date.today())

    def __str__(self):
        return f"{self.CustomerID}'s {self.Product}"