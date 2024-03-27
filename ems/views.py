from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from .models import Salary
from .models import User
from django.db.models import Q
from django.core.paginator import Paginator, Page, EmptyPage, InvalidPage
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.

def allemployees(request):
    employees = Employee.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(employees, 10)  # 10 items per page
    try:
      page_obj = paginator.page(page_number)
    except InvalidPage:
      page_obj = paginator.page(1)
    except EmptyPage:
      page_obj = paginator.page(paginator.num_pages)

    # context = {
    #   'employees': page_obj,
    #  }
    return render(request, "ems/allemployees.html", {"allemployees": page_obj})


def singleemployee(request, empid):
    return render(request, "ems/singleemployee.html")

def addemployee(request):
    if request.method == "POST":
        employeeId =  request.POST.get('employeeId')
        name = request.POST.get('employeeName')
        email = request.POST.get('employeeEmail')
        designation = request.POST.get('employeeDesignation')
        address = request.POST.get('employeeAddress')
        phone = request.POST.get('employeePhone')

        e = Employee()
        e.employeeId = employeeId
        e.name = name
        e.email = email
        e.designation = designation
        e.address = address
        e.phone = phone

        e.save()
        return redirect("/allemployees")
    return render(request, "ems/addemployee.html")


def deleteemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    e.delete()
    return redirect("/allemployees")


def updateemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    return render(request, "ems/updateemployee.html", {"singleemp": e})

def doupdateemployee(request, empid):
    updateemployeeid = request.POST.get('employeeId')
    updatename = request.POST.get('employeeName')
    updateemail = request.POST.get('employeeEmail')
    updatedesignation = request.POST.get('employeeDesignation')
    updateaddress = request.POST.get('employeeAddress')
    updatephone = request.POST.get('employeePhone')

    emp = Employee.objects.get(pk= empid)
    emp.employeeId = updateemployeeid
    emp.name = updatename
    emp.email = updateemail
    emp.designation = updatedesignation
    emp.address = updateaddress
    emp.phone = updatephone
    emp.save()
    return redirect("/allemployees")

def singleemployee(request):
    designation = request.GET.get('designation')
    name = request.GET.get('name')

    if designation and name:
         emp = Employee.objects.filter(
        Q(designation__iexact=designation) & Q(name__icontains=name)
        )
    else:
      emp = Employee.objects.all() 
    return render(request,  "ems/singleemployee.html", {"employees":emp})


def employee_monthly_salary(request, employee_id):
  employee = Employee.objects.get(pk=employee_id)
  salaries = Salary.objects.filter(employee=employee).order_by('-year', '-month')

  # Calculate yearly and monthly totals (optional)
  yearly_totals = {}
  monthly_totals = [0] * 12  # Initialize list for monthly totals (12 months)
  for salary in salaries:
    month = salary.month - 1  # Adjust month index (0-based)
    monthly_totals[month] += salary.net_pay
    if salary.year not in yearly_totals:
      yearly_totals[salary.year] = 0
    yearly_totals[salary.year] += salary.net_pay

  context = {
      'employee': employee,
      'salaries': salaries,
      'yearly_totals': yearly_totals,
      'monthly_totals': monthly_totals,
  }
  return render(request, 'ems/monthly_salary_report.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/login')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'ems/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/allemployees')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'ems/login.html',{'form':form}) 


def logout_view(request):
    logout(request)
    return redirect('login')