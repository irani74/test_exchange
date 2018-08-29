from django.conf.urls import url
from django.urls import path

from accounts.views import Login, Logout

app_name = 'accounts'
urlpatterns = [
#    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    #   path('employee_list/', EmployeeList.as_view(), name='employee_list'),
    #url(r'employee_detail/(?P<employee_id>[0-9]+)/$', EmployeeDetail.as_view(), name='employee_detail'),
   # path('employee_add/', EmployeeAdd.as_view(), name='employee_add'),
    #path('employee_edit/', EmployeeEdit.as_view(), name='employee_edit'),
    #path('employee_remove/', EmployeeRemove.as_view(), name='employee_remove'),
    #path('api/', getApi.as_view(), name='api'),
]
