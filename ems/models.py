from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Employee(models.Model):
    employeeId = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.IntegerField(choices=((1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')))
    year = models.IntegerField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Calculated field

