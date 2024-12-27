# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import MyEmployees
# from .serializers import MyEmployeesSerializer

# # Create your views here.

# @api_view(['GET','POST'])
# def employeesList(request):
#     if request.method=='GET':
#         emp=MyEmployees.objects.all()
#         mySerializer=MyEmployeesSerializer(emp,many=True)
#         return Response(mySerializer.data)
#     elif request.method=='POST':
#         mySerializer=MyEmployeesSerializer(data=request.data)
#         if mySerializer.is_valid():
#             mySerializer.save()
#             return Response(mySerializer.data,status=status.HTTP_201_CREATED)
#         return Response(mySerializer.errors,status=status.HTTP_400_BAD_REQUEST)


from rest_framework import generics
from .models import MyEmployees
from .serializers import MyEmployeesSerializer

class EmployeeList(generics.ListAPIView):
    queryset=MyEmployees.objects.all()
    serializer_class=MyEmployeesSerializer

# class EmployeeList(generics.ListCreateAPIView):     #Retrieving All the values from table
#     queryset=MyEmployees.objects.all()
#     serializer_class=MyEmployeesSerializer

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=MyEmployees.objects.all()
#     serializer_class=MyEmployeesSerializer

