from django.shortcuts import render
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AppointmentSerializer, PatientAppointmentSerializer
from .models import Appointment
from authentication.models import Patient
from authentication.permissions import DoctorPermission, PatientPermission
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, NotFound
import json
from .notification_push import push_notify


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
            for aid in data.get("aids", []):
                appointment = Appointment.objects.get(pk=aid)
                appointment.approved = True
                title = "Appointment Approved"
                body = f"Your appointment request was approved by Dr.{request.user.last_name} {request.user.first_name}"
                patient_uid = appointment.patient.user.uid
                push_notify(patient_uid, title, body)
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


# Pusher Beams AUTH
class BeamsAuthView(views.APIView):
    permission_classes = [IsAuthenticated, PatientPermission]

    def get(self, request, format=None):
        from pusher_push_notifications import PushNotifications

        push_client = PushNotifications(
            instance_id="bf43c259-1895-47cd-83cf-82461abe58b5",
            secret_key="339532172AF3778E9C25495695A9CBA34269183BFE57B0D5DE2739D5290A0109",
        )
        user_id = str(request.user.uid)
        beams_token = push_client.generate_token(user_id)
        # content = {
        #     'user': request.user.first_name,
        #     'user_id': request.user.uid,
        #     'beams_token': beams_token,
        #     'auth': request.auth,
        # }
        return Response(beams_token)
