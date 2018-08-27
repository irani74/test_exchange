from django.db import models
from datetime import datetime



# اطلاعات اضافی کاربر به این مدل اضافه میشود
from accounts.models import ROLE_TYPES




MONEY_TYPE_EURO = 'euro'
MONEY_TYPE_TOMAN = 'toman'
MONEY_TYPE_DOLLAR = 'dollar'
MONEY_TYPES = [
    (MONEY_TYPE_DOLLAR, 'دلار'),
    (MONEY_TYPE_EURO, 'یورو'),
    (MONEY_TYPE_TOMAN, 'تومان'),
]


PAY_TYPE_PAYMENT = 'payment'
PAY_TYPES_GET = 'get'
PAY_TYPES = [
    (PAY_TYPE_PAYMENT, 'پرداخت'),
    (PAY_TYPES_GET, 'برداشت'),
]




class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']




class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    publication_date = models.DateField()








class TransactionCost(models.Model):
    #user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE, null=True, blank=True)

    pay_type = models.CharField(max_length=10 ,choices=PAY_TYPES, null=True, blank=True, verbose_name='واریز یا برداشت')
    money_type = models.CharField(max_length=10 ,choices=MONEY_TYPES , null=True, blank=True, verbose_name='نوع پول')
    start = models.IntegerField( default= 2,  null=True, blank=True, verbose_name='شروع بازه')
    end = models.IntegerField(default= 200, null=True, blank=True, verbose_name='انتهای بازه')
    percent = models.FloatField(max_length=5 , default= 2 ,  null=True, blank=True, verbose_name='درصد کارمزد')

