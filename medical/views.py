from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import DoctorPermission, PatientPermission
from rest_framework.response import Response
from django.http import Http404
from .serializers import *
from .models import *


class MedicalExamViewSet(viewsets.ModelViewSet):
    """
    Medical Exam Modelviewset
    """

    queryset = MedicalExam.objects.all()
    serializer_class = MedicalExamSerializer
    permission_classes = [IsAuthenticated, DoctorPermission]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
    Medical record ModelViewSet
    """

    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAuthenticated, DoctorPermission]
    search_fields = [
        "patient__user__first_name",
        "patient__user__last_name",
        "patient__type",
        "patient__education_level",
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class PatientMedicalRecordAPIView(APIView):
    """
    Retrieve The medical record for the Patient requesting it
    """

    permission_classes = [IsAuthenticated, PatientPermission]

    def get_object(self, patient):
        try:
            return MedicalRecord.objects.get(patient=patient)
        except MedicalRecord.DoesNotExist:
            raise Http404

    def get(self, request):
        """
        GET : retrieve medical record for patient
        """
        patient = Patient.objects.get(user=request.user)
        medical_record = self.get_object(patient)
        serializer = MedicalRecordSerializer(medical_record)
        return Response(serializer.data)
