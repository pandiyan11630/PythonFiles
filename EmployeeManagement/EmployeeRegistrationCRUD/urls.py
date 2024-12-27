from django.urls import path
from . import views

urlpatterns=[
    path('',views.readAllEmployees,name='employeesList'),
    path('addEmployee',views.addNewEmployee,name="addEmployee")
]
