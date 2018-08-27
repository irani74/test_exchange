from django import forms
from django.contrib.auth.models import User

from accounts.models import ROLE_TYPE_EMPLOYEE, ROLE_TYPE_CUSTOMER, ROLE_TYPE_MANAGER
from employee.models import Employee_Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='نام کاربری')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    role_type = ROLE_TYPE_MANAGER

    def clean(self):
        valid_users = User.objects.filter(username=self.cleaned_data['username'], password=self.cleaned_data['password'] , role_type=self.role_type)
        if len(valid_users) < 1:
            raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')


class EmployeeAddForm(forms.Form):
    username = forms.CharField(required=True, label='نام کاربری')
    email = forms.CharField(required=True, label='ایمیل')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, label='نام')
    last_name = forms.CharField(required=True, label='نام خانوادگی')

    def save(self):
        user = User.objects.create(username=self.cleaned_data['username'],
                                   password=self.cleaned_data['password'],
                                   email=self.cleaned_data['email'],
                                   first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'],
                                   role_type=ROLE_TYPE_EMPLOYEE ,
                                   )
        Employee_Profile.objects.create(user=user,
                               role=ROLE_TYPE_EMPLOYEE)



