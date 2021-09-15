from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import *
from authentication.models import *
from authentication.serializers import *


class UserFiltredSerializer(serializers.ModelSerializer):
    """
    User serializer for nested user in patient
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "date_of_birth"]


class PatientFiltredSerializer(serializers.ModelSerializer):
    """
    Patient serializer for medical exams and records
    """

    user = UserFiltredSerializer()

    class Meta:
        model = Patient
        fields = ["pid", "user", "type", "education_level"]


class MedicalRecordSerializer(serializers.ModelSerializer):
    """
    Medical Record serializer
    """

    patient_data = PatientFiltredSerializer(source="patient", read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = MedicalRecord
        fields = "__all__"


class EvacuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evacuation
        fields = "__all__"


class OrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientation
        fields = "__all__"


class MedicalCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCertificate
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"


class MedicalExamSerializer(serializers.ModelSerializer):
    """
    Medical Exam serializer
    """

    patient_data = PatientFiltredSerializer(source="patient", read_only=True)
    doctor_data = UserFiltredSerializer(source="doctor", read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    clinical_exam = serializers.CharField(
        source="clinical_exam.clinical_exam", read_only=True
    )
    paraclinical_exam = serializers.FileField(
        source="paraclinical_exam.paraclinical_exam", use_url=True, read_only=True
    )
    evacuation = EvacuationSerializer(read_only=True)
    orientation = OrientationSerializer(read_only=True)
    medical_certificate = MedicalCertificateSerializer(read_only=True)
    ordanance = PrescriptionSerializer(
        source="prescriptions", many=True, read_only=True
    )

    class Meta:
        model = MedicalExam
        fields = "__all__"

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["doctor"] = request.user
        return super().create(validated_data)


class PraclinicalExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParaclinicalExam
        fields = "__all__"
