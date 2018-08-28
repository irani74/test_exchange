
from django.db import models
from datetime import datetime


# اطلاعات اضافی کاربر به این مدل اضافه میشود
from accounts.models import ROLE_TYPES
from transactions.models import PAY_TYPES, MONEY_TYPES


class Messages(models.Model):
    message = models.TextField( null=True, blank=True)
    subject = models.CharField(max_length=110, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)

