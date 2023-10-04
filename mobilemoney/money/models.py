from django.db import models

class Agent(models.Model):
    GENDER_CHOICES = [
       ( "M", "MALE"),
       ( "F", "FEMALE")
    ]
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    address = models.CharField(max_length=60, null=True, blank=True, default="none" )
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    def __str__(self):
        return f"{self.name}-{self.contact}-{self.address}-{self.agent}"     


class Transfer(models.Model):
    transfer_rate = models.IntegerField()
    amount_transfered = models.IntegerField()
    transfer_date = models.DateField(auto_now=False)  
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.transfer_rate}-{self.amount_transfered}-{self.transfer_date}-{self.agent}" 
    
class Account(models.Model):
    account_name = models.CharField(max_length=50, null=True, blank=True,default="N/A")
    account_balance = models.IntegerField()
    account_rate = models.IntegerField()
    customer_name = models.CharField(max_length=50) 
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.account_name}-{self.account_balance}-{self.account_rate}-{self.customer_name}-{self.agent}"     
    



class   Withdraw(models.Model):
    Withdraw_type = models.CharField(max_length=20, null=True, blank=True,default="N/A")
    Withdraw_date = models.DateField(auto_now=False) 
    Withdraw_amount = models.IntegerField()
    customer_name = models.CharField(max_length=50) 
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{self.Withdraw_type}-{self.Withdraw_date}-{self.Withdraw_amount}-{self.customer_name}-{self.agent}"      


class Deposit(models.Model):
    Deposit_type = models.CharField(max_length=20, null=True, blank=True,default="N/A")
    Deposit_date = models.DateField(auto_now=False) 
    Deposit_amount = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.Deposit_type}-{self.Deposit_date}-{self.Deposit_amount}-{self.customer_name}-{self.agent}"    




    
