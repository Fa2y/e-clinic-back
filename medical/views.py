from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ParseError
from .serializers import *
from .models import *

# Create your views here.

class MedicalExamViewSet(viewsets.ModelViewSet):
    '''
    Medical Exam Modelviewset
    '''
    queryset=MedicalExam.objects.all()
    serializer_class=MedicalExamSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context




class MedicalRecordViewSet(viewsets.ModelViewSet):
    '''
    Medical record ModelViewSet
    '''
    queryset=MedicalRecord.objects.all()
    serializer_class=MedicalRecordSerializer
     
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    