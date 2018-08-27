from django import forms
from django.contrib.auth.models import User

from accounts.models import ROLE_TYPE_EMPLOYEE
from employee.models import Employee_Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='نام کاربری')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    role_type = ROLE_TYPE_EMPLOYEE

    def clean(self):
        valid_users = User.objects.filter(username=self.cleaned_data['username'], password=self.cleaned_data['password'] , role_type=self.role_type)
        if len(valid_users) < 1:
            raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')




