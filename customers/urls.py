from django.conf.urls import url
from django.urls import path

from customers.views import Signup, Login, Logout

app_name = 'customers'
urlpatterns = [
    url('signup/', Signup.as_view(), name='signup'),
    url('login/', Login.as_view(), name='login'),
    url('logout/', Logout.as_view(), name='logout'),

    # url('employee_list/', EmployeeList.as_view(), name='employee_list'),
    # url(r'employee_detail/(?P<employee_id>[0-9]+)/$', EmployeeDetail.as_view(), name='employee_detail'),
    # url('employee_add/', EmployeeAdd.as_view(), name='employee_add'),
    # url('employee_edit/', EmployeeEdit.as_view(), name='employee_edit'),
    # url('employee_remove/', EmployeeRemove.as_view(), name='employee_remove'),
    # url('api/', getApi.as_view(), name='api'),
]
