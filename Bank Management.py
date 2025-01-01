class Account(models.Model):
    ACCOUNT_TYPES = (
        ('Savings', 'Savings Account'),
        ('Current', 'Current Account'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.account_type}"
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.transaction_type == 'Deposit':
            self.account.balance += self.amount
        elif self.transaction_type == 'Withdrawal':
            if self.amount > self.account.balance:
                raise ValueError("Insufficient balance")
            self.account.balance -= self.amount
        self.account.save()
        super().save(*args, **kwargs)
from celery import shared_task
from .models import Account

@shared_task
def calculate_monthly_interest():
    for account in Account.objects.filter(account_type='Savings'):
        interest = account.balance * 0.03  # 3% monthly interest
        account.balance += interest
        account.save()