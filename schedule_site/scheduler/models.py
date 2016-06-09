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

class WorkRole(models.Model):
    """The role performed by an employee"""
    role = models.CharField(
        max_length=2,
        choices=AVAILABLE_ROLES,
    )
