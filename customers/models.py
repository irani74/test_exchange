
from django.db import models
from datetime import datetime


# اطلاعات اضافی کاربر به این مدل اضافه میشود
from accounts.models import ROLE_TYPES
from transactions.models import PAY_TYPES, MONEY_TYPES



class Customers_Profile(models.Model):
    user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_TYPES, null=True, blank=True)

    mobile = models.CharField(max_length=15, null=True, blank=True)
    #fixed_phone = models.CharField(max_length=15, null=True, blank=True)
    shaba = models.CharField(max_length=30, null=True, blank=True)

    #account_id = models.ForeignKey(to=user , on_delete=models.CASCADE ,related_name='')
#####################################################
class Wallet(models.Model):
    wallet_customer = models.OneToOneField(to='Customers_Profile', on_delete=models.CASCADE, null=True, blank=True)

    dollar = models.IntegerField( default=0, null=True, blank=True)
    euro = models.IntegerField( default=0,  null=True, blank=True)
    toman = models.IntegerField( default=0 ,  null=True, blank=True)




class CustomerTransaction(models.Model):

    pay_type = models.CharField(max_length=10 ,choices=PAY_TYPES, null=True, blank=True, verbose_name='واریز یا برداشت')
    money_type = models.CharField(max_length=10 ,choices=MONEY_TYPES , null=True, blank=True, verbose_name='نوع پول')
    payment = models.IntegerField( default= 2,  null=True, blank=True, verbose_name='مبلغ پرداخت')
    job_cost = models.IntegerField( default= 200, null=True, blank=True, verbose_name='کارمزد')
    datetime = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name='زمان')












#class FormModel(models.Model):
#    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام')


#class FieldModel(models.Model):
#    form = models.ForeignKey(to='customers.FormModel', on_delete=models.CASCADE, null=True, blank=True,
#                             verbose_name='فرم')
#    label = models.CharField(max_length=50, null=True, blank=True, verbose_name='برچسب')
#    value = models.CharField(max_length=200, null=True, blank=True, verbose_name='مقدار')

