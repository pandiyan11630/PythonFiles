from django.db import models

# Create your models here.
class MyEmployees(models.Model):
    employee_id=models.AutoField(primary_key=True)
    employee_Name=models.CharField(max_length=10)
    employee_salary=models.FloatField()
    department_name=models.CharField(max_length=10)