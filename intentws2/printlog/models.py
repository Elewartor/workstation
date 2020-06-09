from django.db import models
from account.models import Account
from workstation.models import Unit

# Create your models here.

# label_types = [
#     ('EBL', 'ExtraBoxLabel'),
#     ('BLL', 'BoxLabel'),
#     ('LUL', 'LogitechUnitLabel'),
# ]

class PrintLog(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    date_printed = models.DateTimeField(auto_now=True)
    copies_printed = models.CharField(max_length=2)
    label_type = models.CharField(max_length=3)
    
    def __str__(self):
        return str(self.pk)