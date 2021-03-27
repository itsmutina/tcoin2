from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64, null = True)
    phone = models.CharField(max_length=12, null = True)
    email = models.CharField(max_length=64, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    balance = models.IntegerField(null = True)
    withdrawn = models.IntegerField(null = True)

    def __str__(self):
        return self.name

class Amount(models.Model):
    #person = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
      
    money_earned = models.IntegerField(null = True)

    def __str__(self):
        return self.balance, self.withdrawn

