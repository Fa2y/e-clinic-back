from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import *
from authentication.models import *
from authentication.serializers import *


class UserFiltredSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class PatientFiltredSerializer(serializers.ModelSerializer):

    user = UserFiltredSerializer()

    class Meta:
        model = Patient
        fields = ["pid", "user", "type", "education_level"]


class MedicalExamSerializer(serializers.ModelSerializer):
    """
    medical exam serializer
    """

    patient_data = PatientFiltredSerializer(source="patient", read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    def create(self, validated_data):
        request = self.context["request"]
        validated_data[
            "doctor_name"
        ] = f"Dr. {request.user.last_name} {request.user.first_name}"
        return super().create(validated_data)

    class Meta:
        model = MedicalExam
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    """medical record serializer"""

    patient_data = PatientFiltredSerializer(source="patient", read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    screening = MedicalExamSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = MedicalRecord
        fields = "__all__"

    # def create(self, validated_data):
    #     print(validated_data)
    #     pass
