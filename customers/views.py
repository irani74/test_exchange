from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
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
            return redirect('accounts:home_page')
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
        return render(request, 'tehran payment/default.htm', {
            'form': form,
        })

    @staticmethod
    def post(request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['email'], password=request.POST['password'] )
            if user is not None:
                login(request, user)
                return redirect('accounts/employee/employee_list.html')
        return render(request, 'accounts/authentication/login.html', {
            'form': form,
        })


class Logout(View):
    @staticmethod
    def post(request):
        logout(request.user)
        #redirect


class EditProfile(View):
    @staticmethod
    def get(request):
        form = Edit_ProfileForm()
        return render(request, 'Edit_ProfileForm.html', {
            'form': form,
        })

    @staticmethod
    def post(request):
        form = Edit_ProfileForm(request.POST)
        if form.is_valid():
            #profile =
            form.save()
            #حتما نباید لاگین شه
            #login(request, profile.user)
            #ادرس صفحه ی بعد از عضویت. یا لاگ این. یا تایید با ایمیل
            return redirect('')#url
        return render(request, 'Edit_ProfileForm.html', {
            'form': form, #changed ??????
        })



class Payment(View):
    pass

class Transaction_History(View):
    pass

class Exchange(View):
    pass

