from django.shortcuts import render
from django.template import loader

from .csv_handling import import_staff_from_csv

def import_staff_info(request):
    """Import information about staff availability and shift requirements"""
    path_to_staff = "staff.csv"
    import_staff_from_csv(path_to_staff)

    template = loader.get_template('scheduler/import.html')
    html = template.render(
        { #todo render the staff that were just imported
        },
        request
    )
    return HttpResponse(html)

