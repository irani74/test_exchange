from django.db import models


ROLE_TYPE_MANAGER = 'manager'
ROLE_TYPE_EMPLOYEE = 'employee'
ROLE_TYPE_CUSTOMER = 'customer'
ROLE_TYPES = [
    (ROLE_TYPE_MANAGER, 'مدیر'),
    (ROLE_TYPE_EMPLOYEE, 'کارمند'),
    (ROLE_TYPE_CUSTOMER, 'مشتری'),
]


# اطلاعات اضافی کاربر به این مدل اضافه میشود
#class Profile(models.Model):
    #user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE, null=True, blank=True)
    #role = models.CharField(max_length=20, choices=ROLE_TYPES, null=True, blank=True)
    # temp = models.ManyToManyField()
    # temp = models.ForeignKey()


