# Generated by Django 5.1.4 on 2024-12-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyEmployees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_Name', models.CharField(max_length=10)),
                ('employee_salary', models.FloatField()),
                ('department_name', models.CharField(max_length=10)),
            ],
        ),
    ]
