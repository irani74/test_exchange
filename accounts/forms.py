
from accounts.models import ROLE_TYPE_EMPLOYEE, ROLE_TYPE_CUSTOMER

from django import forms
from django.contrib.auth.models import User

from accounts.models import ROLE_TYPE_CUSTOMER
from customers.models import Customers_Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='ایمیل')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    #role_type = ROLE_TYPE_CUSTOMER

    def clean(self):
        valid_users = User.objects.filter(username=self.cleaned_data['username'], password=self.cleaned_data['password'] )#, customers_profile__role=ROLE_TYPE_CUSTOMER)
        if len(valid_users) < 1:
            raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')
        return 1

