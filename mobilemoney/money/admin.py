from django.contrib import admin

# Register your models here.

from .models import Agent, Account, Transfer, Withdraw, Deposit

class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "address", "gender")
admin.site.register(Agent,AgentAdmin)
def __str__(self):
    return f"{self.name}-{self.contact}-{self.address}-{self.gender}" 


class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_name", "account_balance", "account_rate", "customer_name", "agent")
admin.site.register(Account,AccountAdmin)
def __str__(self):
    return f"{self.account_name}-{self.account_balance}-{self.account_rate}-{self.customer_name}-{self.agent}"  


class TransferAdmin(admin.ModelAdmin):
    list_display = ("transfer_rate", "amount_transfered", "transfer_date", "agent")
admin.site.register(Transfer,TransferAdmin)
def __str__(self):
    return f"{self.transfer_rate}-{self.amount_transfered}-{self.transfer_date}-{self.agent}" 




class WithdrawAdmin(admin.ModelAdmin):
    list_display = ("Withdraw_type", "Withdraw_date", "Withdraw_amount", "customer_name","agent")
admin.site.register(Withdraw,WithdrawAdmin)
def __str__(self):
    return f"{self.Withdraw_type}-{self.Withdraw_date}-{self.Withdraw_amount}-{self.customer_name}-{self.agent}"


class DepositAdmin(admin.ModelAdmin):
    list_display = ("Deposit_type", "Deposit_date", "Deposit_amount", "customer_name","agent")
admin.site.register(Deposit,DepositAdmin)
def __str__(self):
    return f"{self.Deposit_type}-{self.Deposit_date}-{self.Deposit_amount}-{self.customer_name}-{self.agent}"
