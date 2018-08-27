from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile, ROLE_TYPE_EMPLOYEE, ROLE_TYPE_CUSTOMER


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='نام کاربری')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)

    def clean(self):
        valid_users = User.objects.filter(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if len(valid_users) < 1:
            raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')


class SignupForm(forms.Form):
    email = forms.CharField(required=True, label='ایمیل')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, label='نام')
    last_name = forms.CharField(required=True, label='نام خانوادگی')

    def save(self):
        user = User.objects.create(username=self.cleaned_data['email'],
                                   password=self.cleaned_data['password'],
                                   email=self.cleaned_data['email'],
                                   first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'])
        profile = Profile.objects.create(user=user,
                                         role=ROLE_TYPE_CUSTOMER)
        return profile

    def clean_email(self):
        users = User.objects.filter(email=self.cleaned_data['email'])
        if len(users) > 0:
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است.')
        return self.cleaned_data['email']

    def clean_password(self):
        if len(self.cleaned_data['password']) < 8:
            raise forms.ValidationError('رمز باید بیشتر از 8 حرف باشد.')
        return self.cleaned_data['password']


class EmployeeAddForm(forms.Form):
    email = forms.CharField(required=True, label='ایمیل')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, label='نام')
    last_name = forms.CharField(required=True, label='نام خانوادگی')

    def save(self):
        user = User.objects.create(username=self.cleaned_data['email'],
                                   password=self.cleaned_data['password'],
                                   email=self.cleaned_data['email'],
                                   first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'])
        Profile.objects.create(user=user,
                               role=ROLE_TYPE_EMPLOYEE)



