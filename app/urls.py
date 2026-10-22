from django.urls import path
from . import views

urlpatterns =[
    path('CustomerManagementMenu', views.CustomerManagementMenu, name='CustomerManagementMenu'),
    path('CustomerSearch', views.CustomerSearch, name='CustomerSearch'),
]