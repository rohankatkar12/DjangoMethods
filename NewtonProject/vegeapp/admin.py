from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Receipe)
class ReciepeAdmin(admin.ModelAdmin):
    list_display = ['receipe_name', 'receipe_description', 'receipe_image']