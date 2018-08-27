from django.shortcuts import render

# Create your views here.
from django.views import View

from employee.models import Employee_Profile


def is_active_employee(user):
    profiles = Employee_Profile.objects.filter(user=user)
    if len(profiles) > 0 and profiles[0].role is 'employee':
        return True
    return False


class EmployeeEdit(View):
    pass



class Logout(View):
    pass



class Transaction_History(View):
    pass


class Transction_Certification(View):
    pass

