
from django.urls import path, include
from contact.views import contact, thanks

app_name = 'contact'
urlpatterns = [
    path('us/', contact, name='contact'),
    path('thanks/', thanks, name='thanks'),

]




