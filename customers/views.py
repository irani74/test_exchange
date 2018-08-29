from django.contrib.auth import authenticate, login, logout
from django.contrib import sessions
from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import ROLE_TYPE_CUSTOMER
from customers.forms import LoginForm, SignupForm, Edit_ProfileForm
from customers.models import Customers_Profile
from customers.templates import *


class Signup(View):
    @staticmethod
    def get(request):
        form = SignupForm()
        return render(request, 'accounts/authentication/signup.html', {
            'form': form,
        })

    @staticmethod
    def post(request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request, profile.user)
            return redirect('home_page')
        return render(request, 'accounts/authentication/signup.html', {
            'form': form,
        })




############################################################
def is_login(user):
    # return True
    profiles = User.objects.filter(user=user)
    if len(profiles) > 0 :
        return True
    return False
#############################################################






class Login(View):
    @staticmethod
    def get(request):
        form = LoginForm()
        return render(request, 'accounts/authentication/login.html', {
            'form': form,
        })

    @staticmethod
    def post(request):
        form = LoginForm(request.POST)
        print('in post')

        if form.is_valid():
            print('in first if')
            #password = form.cleaned_data['password']
            #username = request.POST['username']

            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'] )

            print(user)
            print('user must be printed')
            if (user is not None) or (Customers_Profile.user != ROLE_TYPE_CUSTOMER):
                print('user not none ')
                login(request, user)
                #request.session['UserId'] = user.id
                #request.session['ProfileId'] = user.Cus

                return redirect(reverse('home_page'))


        return render(request, 'accounts/authentication/login.html', {
            'form': form,
        })



class EditProfile(View):
    @staticmethod
    def get(request):
        form = Edit_ProfileForm()
        #user = request.session['User']
        print('username:')

        customer_profile=Customers_Profile.objects.get(user=request.user)

        print('role:')
        print(customer_profile.role)
        print('mobile:')
        print(customer_profile.mobile)
        print('fixed:')
        print(customer_profile.fixed_phone)
        print('shaba:')
        print(customer_profile.shaba)
        form.shaba = customer_profile.shaba
        form.mobile = customer_profile.mobile
        form.fixed_phone = customer_profile.fixed_phone

        return render(request, 'accounts/edit_profile.html', {
            'form': form,
        })



    @staticmethod
    def post(request):
        form = Edit_ProfileForm(request.POST)
        if form.is_valid():

            #profile =
            print('save form')
            userProfile = Customers_Profile.objects.get(user=request.user)

            userProfile.update(mobile=form.cleaned_data['mobile'],
                                fixed_phone=form.cleaned_data['fixed_phone'],
                                shaba=form.cleaned_data['shaba'],
                                )


            #form.save(user)
            #print(form)
            #حتما نباید لاگین شه
            #login(request, profile.user)
            #ادرس صفحه ی بعد از عضویت. یا لاگ این. یا تایید با ایمیل
            return redirect('contact:thanks')#url
        return render(request, 'accounts/edit_profile.html', {
            'form': form, #changed ??????
        })



class Payment(View):
    pass

class Transaction_History(View):
    pass

class Exchange(View):
    pass

