from django.shortcuts import render, redirect
from django.views import View

import json
import requests

from transactions.forms import TransactionCostForm
from transactions.models import TransactionCost

class Addition(View):
    pass




#class getApi(View):
#    pass


DOLLAR = 0
EURO = 0





class CurencyNow(View):

    final_dollar_price=0
    final_euro_price=0

    #@staticmethod
    #def nowCost(self):

    @staticmethod
    def get(request):
        r = requests.get('http://call.tgju.org/ajax.json')
        #print(r.text)
        result = json.loads(r.text)
        dollar_price = result['current']['price_dollar']['p']
        euro_price = result['current']['price_eur']['p']
        dollar_price = dollar_price.split(',')
        euro_price = euro_price.split(',')
        final_dollar_price = ''
        final_euro_price = ''
        for i in dollar_price:
            final_dollar_price = final_dollar_price + i
        for i in euro_price:
            final_euro_price = final_euro_price + i

        final_dollar_price = int(final_dollar_price)/10
        final_euro_price = int(final_euro_price)/10

        CURENCY = [
            (final_dollar_price, 'دلار'),
            (final_euro_price, 'یورو'),
        ]

        EURO = final_euro_price
        DOLLAR = final_dollar_price

        print(final_dollar_price)
        print(final_euro_price)


        return render(request, 'curency_now.html', {

                'form':CURENCY ,

        })

    #def euro(self):
    #    return int(self.final_euro_price)

    #def dollar(self):
    #    return int(self.final_dollar_price)


        # form = LoginForm()
        #CurencyNow.nowCost
        #dollar=re
        #euro=request.nowCost




#class EmployeeList(View):
 #   @staticmethod
  #  def get(request):
   #     employees = Employee_Profile.objects.filter(role=ROLE_TYPE_EMPLOYEE)
    #    return render(request, 'accounts/employee/employee_list.html', context={
     #       'employees': employees,
      #  })

class TransactionsCosts(View):

    @staticmethod
    def get(request):
        form = TransactionCost.objects.all()
        return render(request, 'transaction_cost.html' ,context={

                    'form': form}
                      )

    def new_item(self):
        TransactionCost.objects.all().delete()
        TransactionCost.objects.create(pay_type='تبدیل به دلار', money_type='تومان', start=10000, end=1000000,
                                       percent=5)
        TransactionCost.objects.create(pay_type='تبدیل به ریال', money_type='دلار', start=10, end=100, percent=2)
        TransactionCost.objects.create(pay_type='تبدیل به یورو', money_type='تومان', start=10000, end=100000, percent=6)
        TransactionCost.objects.create(pay_type='واریز به حساب داخلی', money_type='تومان', start=1000, end=1000000,
                                       percent=3)
        TransactionCost.objects.create(pay_type='واریز به حساب دلار', money_type='دلار', start=10, end=100, percent=7)
        TransactionCost.objects.create(pay_type='واریز به حساب یورو', money_type='یورو', start=10, end=100, percent=5)
        return redirect('contact:thanks')#url


class TestExchange(View):

    @staticmethod
    def get(request):
        form = TransactionCost.objects.all()
        return render(request, 'transaction_cost.html' ,context={

                    'form': form}
                      )


    @staticmethod
    def post(request):
        pass




class Signup(View):
    @staticmethod
    def get(request):
        #form = SignupForm()
        return render(request, 'accounts/authentication/signup.html', {
            #'form': form,
        })

    @staticmethod
    def post(request):
        #form = SignupForm(request.POST)
        #if form.is_valid():
         #   form.save()
            #login(request, profile.user)
            #return redirect('home_page')
        return render(request, 'accounts/authentication/signup.html', {
            #'form': form,
        })


