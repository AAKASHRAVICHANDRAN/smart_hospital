from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# ---------------------- CUSTOM USER ----------------------

class User(AbstractUser):
    ROLE_CHOICES = (
        ("doctor", "Doctor"),
        ("patient", "Patient"),
        ("receptionist", "Receptionist"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="patient")

    def is_doctor(self):
        return self.role == "doctor"

    def is_patient(self):
        return self.role == "patient"

    def is_receptionist(self):
        return self.role == "receptionist"


# ---------------------- APPOINTMENT MODEL ----------------------
# Use unique related_names to prevent conflicts with hospital.Appointment

class Appointment(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="accounts_patient_appointments"
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="accounts_doctor_appointments"
    )
    datetime = models.DateTimeField()
    status = models.CharField(
        max_length=50, 
        choices=[("Scheduled", "Scheduled"), ("Completed", "Completed"), ("Cancelled", "Cancelled")],
        default="Scheduled"
    )

    def __str__(self):
        return f"Appointment {self.id} - {self.patient.username} with {self.doctor.username}"
