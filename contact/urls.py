
from django.urls import path, include
from contact.views import contact, thanks

app_name = 'contact'
urlpatterns = [
    path('contact/', contact, name='contact'),
    path('thanks/', thanks, name='thanks'),

]




