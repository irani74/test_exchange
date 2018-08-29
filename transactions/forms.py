from django import forms
from transactions.models import TransactionCost
from django.shortcuts import render
from django.views import View
DOLLAR =0
EURO = 0
CURENCY = [
    (DOLLAR, 'دلار'),
    (EURO, 'یورو'),
]

class CurencyNowForm(forms.Form):

    #euro , dollar = getApi()

    #dollar = forms.CharField(required=True, label='ایمیل')
    #euro = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    pass



class TransactionCostForm(forms.Form):

    def clean(self):
        print('cleaned')
        return TransactionCost.objects.all()




class TestExchange(forms.Form):
    start = forms.IntegerField(required=True, label='مبلغ ارز مبدا')
    end = forms.IntegerField(required=True, label='مبلغ دریافتی ارز مقصد')
    moneyType = forms.CharField(required=True, label='نوع ارز دریافتی')


    # role_type = ROLE_TYPE_CUSTOMER

    def clean(self):
        pass
        #valid_users = User.objects.filter(username=self.cleaned_data['username'], password=self.cleaned_data[
         #   'password'])  # , customers_profile__role=ROLE_TYPE_CUSTOMER)
        #if  :
         #   raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')

