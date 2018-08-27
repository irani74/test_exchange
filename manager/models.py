
from django.db import models
from datetime import datetime


# اطلاعات اضافی کاربر به این مدل اضافه میشود
from accounts.models import ROLE_TYPES


class Manager_Profile(models.Model):
    user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_TYPES, null=True, blank=True)

    # temp = models.ManyToManyField()
    # = models.ForeignKey()
    #account_id = models.ForeignKey(to=user , on_delete=models.CASCADE ,related_name='')
#####################################################
    dollarMax = models.IntegerField( default=20000, null=True, blank=True)
    dollarMin = models.IntegerField( default=20, null=True, blank=True)
    euroMax = models.IntegerField( default=20000,  null=True, blank=True)
    euroMin = models.IntegerField( default=20, null=True, blank=True)
    tomanMax = models.IntegerField( default=400000000 ,  null=True, blank=True)
    tomanMin = models.IntegerField( default=40000 , null=True, blank=True)

    salaryDate = models.IntegerField( default=1 , null=True, blank=True)



class AccessLog(models.Model):
    # field_name = models.ForeignKey(to='app_name.model_name')
    manager = models.ForeignKey(to='manager.Manager_Profile', on_delete=models.DO_NOTHING, null=True, blank=True,
                                verbose_name='مدیر')
    customer = models.ForeignKey(to='customers.Customers_Profile', on_delete=models.DO_NOTHING, null=True, blank=True,
                                 verbose_name='مشتری')
    datetime = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name='زمان')
    # number = models.IntegerField(null=True,)


class MoneyTransaction(models.Model):
    pass


