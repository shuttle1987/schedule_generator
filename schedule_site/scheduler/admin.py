from django.contrib import admin

from .models import (
    WorkRole,
    Employee,
    Day,
)

admin.site.register(WorkRole)
admin.site.register(Employee)
admin.site.register(Day)
