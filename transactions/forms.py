from django.forms import Form, forms
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



    def clean(self):
        pass