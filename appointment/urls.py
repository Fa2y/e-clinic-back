from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"appointments", DoctorAppointmentViewSet)
router.register(r"patient-appointments", PatientAppointmentViewSet)
urlpatterns = [
    path("api-appointment/", include(router.urls)),
    path(r"api-appointment/beams-auth/", BeamsAuthView.as_view()),
]
