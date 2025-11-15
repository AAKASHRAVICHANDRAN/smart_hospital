from django.urls import path
from . import views

app_name = "hospital"

urlpatterns = [
    path("appointments/", views.appointments_list, name="appointments_list"),
    path("appointments/create/", views.appointment_create, name="appointment_create"),
    path("appointments/<int:pk>/edit/", views.appointment_edit, name="appointment_edit"),
    path("appointments/<int:pk>/delete/", views.appointment_delete, name="appointment_delete"),

    path("records/", views.records_list, name="records_list"),
    path("records/create/", views.record_create, name="record_create"),
]
