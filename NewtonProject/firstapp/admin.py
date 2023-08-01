from django.contrib import admin
from .models import *


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "contact", "address"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "email", "address", "contact"]

@admin.register(Car)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "car_name", "speed"]
