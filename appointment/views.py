from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AppointmentSerializer, PatientAppointmentSerializer
from .models import Appointment
from authentication.models import Patient
from authentication.permissions import DoctorPermission, PatientPermission
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, NotFound
import json


class DoctorAppointmentViewSet(viewsets.ModelViewSet):
    """
    Appointment ViewSet For doctor only
    """

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated, DoctorPermission]

    @action(detail=False, methods=["patch"])
    def approve(self, request):
        """
        Approve Multiple Appointments
        """
        try:
            data = json.loads(request.body)
            print(repr(data))
            for aid in data.get("aids", []):
                appointment = Appointment.objects.get(pk=aid)
                appointment.approved = True
                appointment.save()
            return Response(
                {"details": "Appointments approved successfully"},
                status=status.HTTP_202_ACCEPTED,
            )
        except Appointment.DoesNotExist:
            raise NotFound()
        except Exception:
            raise ParseError()


class PatientAppointmentViewSet(viewsets.ModelViewSet):
    """
    Appointment ViewSet For Patients
    """

    serializer_class = PatientAppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated, PatientPermission]

    def get_queryset(self):
        user = self.request.user
        patient = Patient.objects.get(user=user.pk)
        return Appointment.objects.filter(patient=patient)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
