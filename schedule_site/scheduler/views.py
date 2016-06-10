from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .csv_handling import import_staff_from_csv

from .models import Employee

def import_staff_info(request):
    """Import information about staff availability and shift requirements"""
    path_to_staff = "staff.csv"

    try:
        import_staff_from_csv(path_to_staff)
    except FileNotFoundError:
        status = "Could not find staff file"
    else:
        status = "Staff file found"
    template = loader.get_template('scheduler/import.html')
    html = template.render(
        { #todo render the staff that were just imported
            "status": status,
        },
        request
    )
    return HttpResponse(html)

def list_employees(request):
    """List the employees in the database"""
    employees = Employee.objects.all
    template = loader.get_template('scheduler/employees.html')
    html = template.render(
        {
            "employees": employees,
        },
        request
    )
    return HttpResponse(html)

