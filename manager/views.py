from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views import View

from accounts.models import ROLE_TYPE_EMPLOYEE , ROLE_TYPE_MANAGER
from employee.models import Employee_Profile
from manager.forms import EmployeeAddForm
from manager.models import Manager_Profile


class Logout(View):
    pass



class EmployeeList(View):
    @staticmethod
    def get(request):
        employees = Employee_Profile.objects.filter(role=ROLE_TYPE_EMPLOYEE)
        return render(request, 'accounts/employee/employee_list.html', context={
            'employees': employees,
        })


class EmployeeDetail(View):
    @staticmethod
    def get(request, employee_id):
        employee = Employee_Profile.objects.get(id=employee_id)
        return render(request, 'accounts/employee/employee_detail.html', {
            'employee': employee,
        })


def is_admin(user):
    # return True
    profiles = Manager_Profile.objects.filter(user=user)
    if len(profiles) > 0 and profiles[0].role is ROLE_TYPE_MANAGER:
        return True
    return False


@method_decorator([csrf_exempt, user_passes_test(is_admin, login_url='/accounts/login/')], name='dispatch')
class EmployeeAdd(View):
    @staticmethod
    def get(request):
        print(request.user.first_name)
        form = EmployeeAddForm()
        return render(request, 'accounts/employee/employee_add.html', context={
            'form': form,
        })

    @staticmethod
    def post(request):
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reversed('accounts:employee_list'))
        return render(request, 'accounts/employee/employee_add.html', context={
            'form': form,
        })

class Add_Value(View):
    pass

class Transaction_History(View):
    pass


class EmployeeRemove(View):
    pass

class Salary_Payment(View):
    pass
    #time
    #salary value

class Financial(View):
    pass
    #mojoodi
    #gardesh































class EmployeeList(View):
    @staticmethod
    def get(request):
        employees = Profile.objects.filter(role=ROLE_TYPE_EMPLOYEE)
        return render(request, 'accounts/employee/employee_list.html', context={
            'employees': employees,
        })


class EmployeeDetail(View):
    @staticmethod
    def get(request, employee_id):
        employee = Profile.objects.get(id=employee_id)
        return render(request, 'accounts/employee/employee_detail.html', {
            'employee': employee,
        })


def is_admin(user):
    # return True
    profiles = Profile.objects.filter(user=user)
    if len(profiles) > 0 and profiles[0].role is ROLE_TYPE_MANAGER:
        return True
    return False

def is_active_employee(user):
    profiles = Profile.objects.filter(user=user)
    if len(profiles) > 0 and profiles[0].role is 'employee':
        return True
    return False


@method_decorator([csrf_exempt, user_passes_test(is_admin, login_url='/accounts/login/')], name='dispatch')
class EmployeeAdd(View):
    @staticmethod
    def get(request):
        print(request.user.first_name)
        form = EmployeeAddForm()
        return render(request, 'accounts/employee/employee_add.html', context={
            'form': form,
        })

    @staticmethod
    def post(request):
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reversed('accounts:employee_list'))
        return render(request, 'accounts/employee/employee_add.html', context={
            'form': form,
        })


class EmployeeEdit(View):
    pass



