"""test_exchange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from test_exchange.views import About , Laws , HomePage
from transactions.views import TestExchange , CurencyNow , TransactionsCosts
#from accounts.views import HomePage2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('customers/', include('customers.urls')),
    path('employee/', include('employee.urls')),
    path('hesaab/', include('hesaab.urls')),
    path('manager/', include('manager.urls')),
    #path('home/', HomePage2.as_view(), name='home_page2'),
    path('test exchange/', TestExchange.as_view(), name='test_exchanged'),
    path('curency now/', CurencyNow.as_view(), name='curency_now'),
    path('transactions cost/', TestExchange.as_view(), name='transaction_cost'),
    path('', HomePage.as_view(), name='home_page'),



    path('about/', About.as_view(), name='about'),
    path('laws/', Laws.as_view(), name='laws'),
    path('contact/', include('contact.urls')),

]
