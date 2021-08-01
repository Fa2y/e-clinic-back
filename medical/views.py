from rest_framework import viewsets
from .serializers import *
from .models import *


class MedicalExamViewSet(viewsets.ModelViewSet):
    """
    Medical Exam Modelviewset
    """

    queryset = MedicalExam.objects.all()
    serializer_class = MedicalExamSerializer

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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
