from django import forms

class EmployeeForm(forms.Form):
    employee_id=forms.IntegerField()
    employee_Name=forms.CharField(max_length=10)
    employee_salary=forms.FloatField()
    department_name=forms.CharField(max_length=10)