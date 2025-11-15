from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import RegistrationForm
from .models import Appointment

User = get_user_model()

# ---------------------- AUTH VIEWS ----------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_doctor():
                return redirect("accounts:doctor_dashboard")
            if user.is_patient():
                return redirect("accounts:patient_dashboard")
            if user.is_receptionist():
                return redirect("accounts:reception_dashboard")
            return redirect("home")
        return render(request, "accounts/login.html", {"error": "Invalid credentials"})
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_doctor():
                return redirect("accounts:doctor_dashboard")
            if user.is_patient():
                return redirect("accounts:patient_dashboard")
            if user.is_receptionist():
                return redirect("accounts:reception_dashboard")
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


# ---------------------- DASHBOARDS ----------------------

@login_required
def doctor_dashboard(request):
    if not request.user.is_doctor():
        return HttpResponseForbidden("Forbidden")
    return render(request, "accounts/dashboard_doctor.html")


@login_required
def patient_dashboard(request):
    if not request.user.is_patient():
        return HttpResponseForbidden("Forbidden")
    return render(request, "accounts/dashboard_patient.html")


@login_required
def reception_dashboard(request):
    if not request.user.is_receptionist():
        return HttpResponseForbidden("Forbidden")
    return render(request, "accounts/dashboard_receptionist.html")


# ---------------------- RECEPTIONIST PAGES ----------------------

@login_required
def patients_list_view(request):
    if not request.user.is_receptionist():
        return HttpResponseForbidden("Forbidden")
    patients = User.objects.filter(role="patient")
    return render(request, "accounts/patients_list.html", {"patients": patients})


@login_required
def appointments_list_view(request):
    if not request.user.is_receptionist():
        return HttpResponseForbidden("Forbidden")
    appointments = Appointment.objects.all()
    return render(request, "accounts/appointments_list.html", {"appointments": appointments})
