from django.contrib import admin
from .models import Appointment, MedicalRecord

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "start_time", "status")
    list_filter = ("status", "doctor")

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "created_at")
    list_filter = ("doctor",)
