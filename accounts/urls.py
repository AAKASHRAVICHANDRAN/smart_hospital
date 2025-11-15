from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # Auth
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    # Dashboards
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
    path("dashboard/reception/", views.reception_dashboard, name="reception_dashboard"),

    # Receptionist pages
    path("patients/", views.patients_list_view, name="patients_list"),
    path("appointments/", views.appointments_list_view, name="appointments_list"),
]
