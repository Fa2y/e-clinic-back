from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"appointments", DoctorAppointmentViewSet, basename="appointments")
router.register(r"patient-appointments", PatientAppointmentViewSet, basename="patient_appointments")
urlpatterns = [
    path("api-appointment/", include(router.urls)),
]
