from django.urls import path
#from .views import employeesList
#from .views import EmployeeList,EmployeeDetail
from .views import EmployeeList

urlpatterns=[
    #path('getAllEmployees',employeesList,name="getAllEmployees")
    # path('getAllAndInsert',EmployeeList.as_view(),name='getAllAndInsert'),
    # path('getUpdateAndDelete/<int:pk>',EmployeeDetail.as_view(),name='getUpdateAndDelete')
    path('getAllEmpDetails',EmployeeList.as_view(),name='getAllEmpDetails')
]