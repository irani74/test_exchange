
from django.contrib import admin
from django.urls import path, include

from transactions.views import Addition


app_name = 'transactions'
urlpatterns = [
    path('Addition/', Addition.as_view(), name='Addition'),
    #path('contact/', contact, name='contact'),

]
