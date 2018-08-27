from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import LoginForm
from accounts.models import ROLE_TYPE_EMPLOYEE, ROLE_TYPE_MANAGER


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
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['email'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('accounts:home_page')
        return render(request, 'accounts/authentication/login.html', {
            'form': form,
        })


class Logout(View):
    pass

class HomePage(View):

    @staticmethod
    def get(request):
        #form = LoginForm()
        return render(request, 'accounts/base/home_page.html', {
            #'form': form,
        })

