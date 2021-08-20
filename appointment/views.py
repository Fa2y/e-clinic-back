from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppointmentSerializer, PatientAppointmentSerializer
from .models import Appointment
from authentication.models import Patient
from authentication.permissions import DoctorPermission, PatientPermission


class DoctorAppointmentViewSet(viewsets.ModelViewSet):
    """
    Appointment ViewSet For doctor only
    """

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [DoctorPermission]


class PatientAppointmentViewSet(viewsets.ModelViewSet):
    """
    Appointment ViewSet For Patients
    """

    serializer_class = PatientAppointmentSerializer
    queryset = Appointment.objects.all()
    # to do uncomment this line 
    #permission_classes = [PatientPermission]

    def get_queryset(self):
        user = self.request.user
        patient = Patient.objects.get(user=user.pk)
        queryset = Appointment.objects.filter(patient=patient)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
