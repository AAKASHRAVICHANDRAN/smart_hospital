from django import forms
from .models import Appointment, MedicalRecord

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("doctor", "patient", "start_time", "end_time", "reason", "status")
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type":"datetime-local"}),
        }

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ("patient", "doctor", "notes")
