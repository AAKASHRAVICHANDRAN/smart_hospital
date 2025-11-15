from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, MedicalRecord
from .forms import AppointmentForm, MedicalRecordForm
from django.http import HttpResponseForbidden

@login_required
def appointments_list(request):
    # role-aware listing
    if request.user.role == "doctor":
        qs = Appointment.objects.filter(doctor=request.user)
    elif request.user.role == "patient":
        qs = Appointment.objects.filter(patient=request.user)
    elif request.user.role == "receptionist":
        qs = Appointment.objects.all()
    else:
        qs = Appointment.objects.none()
    return render(request, "hospital/appointments_list.html", {"appointments": qs})

@login_required
def appointment_create(request):
    if request.user.role not in ("receptionist", "doctor", "patient"):
        return HttpResponseForbidden()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hospital:appointments_list")
    else:
        form = AppointmentForm()
    return render(request, "hospital/appointment_form.html", {"form": form})

@login_required
def appointment_edit(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    # only doctor/receptionist or owner patient can edit
    if request.user.role not in ("doctor", "receptionist") and appt.patient != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appt)
        if form.is_valid():
            form.save()
            return redirect("hospital:appointments_list")
    else:
        form = AppointmentForm(instance=appt)
    return render(request, "hospital/appointment_form.html", {"form": form, "edit": True})

@login_required
def appointment_delete(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.user.role not in ("doctor", "receptionist") and appt.patient != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        appt.delete()
        return redirect("hospital:appointments_list")
    return render(request, "hospital/appointment_delete.html", {"appointment": appt})

@login_required
def records_list(request):
    if request.user.role == "doctor":
        qs = MedicalRecord.objects.all()
    else:
        qs = MedicalRecord.objects.filter(patient=request.user)
    return render(request, "hospital/records_list.html", {"records": qs})

@login_required
def record_create(request):
    if request.user.role != "doctor":
        return HttpResponseForbidden()
    if request.method == "POST":
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hospital:records_list")
    else:
        form = MedicalRecordForm()
    return render(request, "hospital/record_form.html", {"form": form})
