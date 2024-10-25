from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeField(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    additional_data = models.JSONField(default=dict, blank=True)