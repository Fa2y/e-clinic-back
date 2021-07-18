from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import *
from authentication.models import *
from authentication.serializers import *


class UserFiltredSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name"
        ]




class PatientFiltredSerializer(serializers.ModelSerializer):

    user=UserFiltredSerializer()
    class Meta:
        model=Patient
        fields=[
            "pid",
            "user"
        ]
            
            
        
  


class MedicalExamSerializer(serializers.ModelSerializer):
    '''
    medical exam serializer
    '''
    patient=PatientFiltredSerializer()

    class Meta:
        model= MedicalExam

        fields="__all__"


class MedicalExamFiltredSerializer(serializers.ModelSerializer):
    

    class Meta:
        model= MedicalExam

        fields=[
            
            "id",
            
            "doctor_name",
        ]


class MedicalRecordSerializer(serializers.ModelSerializer):
    '''medical record serializer'''

    patient=PatientFiltredSerializer()
    screening=MedicalExamFiltredSerializer()

    class Meta:
        model=MedicalRecord
        fields="__all__"
    
   