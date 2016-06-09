from django.db import models


MANAGER = 'Manager'
CHEF = 'Chef'
COOK = 'Cook'
DISHWASHER = 'Dishwasher'

AVAILABLE_ROLES = (
    ('0', MANAGER),
    ('1', CHEF),
    ('2', COOK),
    ('3', DISHWASHER),
)

MONDAY = 'Monday'
TUESDAY = 'Tuesday'
WEDNSEDAY = 'Wednseday'
THURSDAY = 'Thursday'
FRIDAY = 'Friday'
SATURDAY = 'Saturday'
SUNDAY = 'Sunday'

DAYS = (
    ('MON', MONDAY),
    ('TUE', TUESDAY),
    ('WED', WEDNSEDAY),
    ('THU', THURSDAY),
    ('FRI', FRIDAY),
    ('SAT', SATURDAY),
    ('SUN', SUNDAY),
)

class WorkRole(models.Model):
    """The role performed by an employee"""
    role = models.CharField(
        max_length=2,
        choices=AVAILABLE_ROLES,
    )

class Employee(models.Model):
    """Information about an Employee"""
    max_hours = models.IntegerField()
    employee_id = models.IntegerField()
    capable_roles = models.ManyToManyField(WorkRole)

class Day(models.Model):
    """Represent a day of the week"""
    day = models.CharField(
        max_length=3,
        choices=DAYS,
    )
