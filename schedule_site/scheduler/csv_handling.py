"""Module containing the parsing code for the staffing information from csv serialized files"""
import csv

from .models import Employee, WorkRole

def import_staff_from_csv(csv_path):
    """Import the CSV staff information"""
    imported_staff = [] #staff imported this run
    with open(csv_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            employee_id = row["Employee ID"]
            valid_roles = row["Valid Roles"]
            max_hours = row["Max Hours"]
            days_unavailable = row["Days Unavailable"]
            
            print("employee_id. valid_roles, max_hours, days_unavailable: ", employee_id, valid_roles, max_hours, days_unavailable)
            
            if created:
                imported_staff.append({
                    "Employee ID": employee_id,
                    "valid_roles": valid_roles,
                    "max_hours": max_hours,
                    "days_unavailable": days_unavailable,
                })

            #employee, created = Employee.objects.get_or_create(
            #    max_hours=max_hours,
            #    employee_id=employee_id,
            #    capable_roles=
            #)
    return imported_staff
