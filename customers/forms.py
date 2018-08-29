from django import forms
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

from accounts.models import ROLE_TYPE_CUSTOMER
from customers.models import Customers_Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='ایمیل')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    role_type = ROLE_TYPE_CUSTOMER

    #def clean(self):
     #   valid_users = User.objects.filter(username=self.cleaned_data['username'],password=self.cleaned_data['password'])
      #  if len(valid_users) < 1:
       #     raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'] )

        if user is None :
            raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')





class SignupForm(forms.Form):
    email = forms.CharField(required=True, label='ایمیل')
    password = forms.CharField(required=True, label='رمز', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, label='نام')
    last_name = forms.CharField(required=True, label='نام خانوادگی')

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['email'],
                                   email=self.cleaned_data['email'],
                                   first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'],
                                   #role=ROLE_TYPE_CUSTOMER,
                                   password=self.cleaned_data['password']
                                   )
        #user2 = User.objects.create(user)

        #user.set_password(self.cleaned_data['password'])
        profile = Customers_Profile.objects.create(user=user,
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



class Edit_ProfileForm(forms.Form):
    #غیر قابل تغییر: نام. نام خانوادگی. ایمیل.
    #قابل تغییر: موبایل. تلفن ثابت. شماره شبا

    mobile = forms.CharField(required=False, label='موبایل' )#,initial=str(Customers_Profile.mobile) )
    fixed_phone = forms.CharField(required=False, label='تلفن ثابت' )#,initial=str(Customers_Profile.fixed_phone ))
    shaba = forms.CharField(required=False, label= 'شماره شبا')#,initial=str(Customers_Profile.shaba ))
    changeed = 0

    def save(self , user):
        self.changeed = 1

        #user = \
        print('shaba in form')
        print(user.shaba)
        user.objects.update(mobile=self.cleaned_data['mobile'],
                                                fixed_phone=self.cleaned_data['fixed_phone'],
                                                shaba=self.cleaned_data['shaba'],
                                                )
        print(user.shaba)
        return user



class PaymentForm(forms.Form):

    value = forms.CharField(required=True, label='مبلغ')

    fish_number = forms.CharField(required=True, label='شماره فیش')

    payment_day = forms.CharField(required=True, label='تاریخ پرداخت')
    payment_hours = forms.CharField(required=True, label='ساعت پرداخت')
    payment_minutes = forms.CharField(required=True, label='دقیقه ی پرداخت')

    card_last_4_number = forms.CharField(required=True, label='4 رقم آخر شماره کارت')


    def clean(self):
        valid_users = User.objects.filter(username=self.cleaned_data['username'], password=self.cleaned_data['password'] , role_type=self.role_type)
        # student.courses.add(course)
        if len(valid_users) < 1:
            raise forms.ValidationError('نام کاربری یا رمز اشتباه است.')



    def save(self):
        self.changeed = 1
        user = Customers_Profile.objects.update(mobile=self.cleaned_data['mobile'],
                                                fixed_phone=self.cleaned_data['fixed_phone'],
                                                shaba=self.cleaned_data['shaba']
                                                )
        return user


class Transaction_HistoryForm(forms.Form):
    pass

class ExchangeForm(forms.Form):
    pass


