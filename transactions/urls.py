
from django.contrib import admin
from django.urls import path, include

from transactions.views import TransactionsCosts


app_name = 'transactions'
urlpatterns = [
    #path('Addition/', Addition.as_view(), name='Addition'),
    path('just first/',TransactionsCosts.new_item , name='just_first'),
    #path('just first/', TransactionsCosts.new_item, name='just_first'),

]
