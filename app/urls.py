from django.urls import path
from . import views

urlpatterns =[
    path('MainMenu', views.MainMenu, name='MainMenu'),
    path('CustomerManagementMenu', views.CustomerManagementMenu, name='CustomerManagementMenu'),
    path('CustomerList', views.CustomerList, name='CustomerList'),
    path('CustomerSearch', views.CustomerSearch, name='CustomerSearch'),
    path('CustomerRegist', views.CustomerRegist, name='CustomerRegist'),
    path('CustomerDelete', views.CustomerDelete, name='CustomerDelete'),
    path('CustomerUpdate', views.CustomerUpdate, name='CustomerUpdate'),
    path('Logout', views.Logout, name='Logout'),
]