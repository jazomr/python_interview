from django.db import models
from python_code_interview.users.models import User


# Create your models here.
class StockSearch(models.Model):
    symbol = models.CharField(max_length=10, null=False)
    price = models.DecimalField(max_digits=14, decimal_places=4)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.symbol)
