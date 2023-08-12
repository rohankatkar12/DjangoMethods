from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department']


@admin.register(StudentId)
class StudentIdAdmin(admin.ModelAdmin):
    list_display = ['student_id']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['department','student_id', 'student_name', 'student_email', 'student_age', 'student_address']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']



class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(SubjectMarks, SubjectMarksAdmin)