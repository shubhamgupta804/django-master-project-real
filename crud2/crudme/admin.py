from django.contrib import admin
from .models import Student,AutoCapture
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')
@admin.register(AutoCapture)
class AutoCaptureAdmin(admin.ModelAdmin):
    list_display = ('image', 'latitude', 'longitude', 'altitude', 'created_at')
    
