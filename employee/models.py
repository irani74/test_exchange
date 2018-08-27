from django.db import models

# Create your models here.
from django.db import models


# اطلاعات اضافی کاربر به این مدل اضافه میشود
class Employee_Profile(models.Model):
    user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE, null=True, blank=True)
    #role = models.CharField(max_length=20, choices=ROLE_TYPES, null=True, blank=True)

    # temp = models.ManyToManyField()
    # = models.ForeignKey()
    #account_id = models.ForeignKey(to='' , on_delete=models.CASCADE ,related_name='')
#####################################################
