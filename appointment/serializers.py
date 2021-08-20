from rest_framework import serializers
from authentication.models import Patient, User
from .models import Appointment


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """

    class Meta:
        model = User
        exclude = (
            "username",
            "password",
            "is_staff",
            "user_permissions",
            "groups",
            "created_on",
        )


class PatientSerializer(serializers.ModelSerializer):
    """
    Patient Serializer
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Appoinment Serializer for doctors
    """

    patient_data = PatientSerializer(source="patient", read_only=True)
    doctor_data = PatientSerializer(source="assigned_to", read_only=True)
    patient = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Patient.objects.all()
    )
    logged_by = serializers.PrimaryKeyRelatedField(read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        validated_data["approved"] = True
        request = self.context["request"]
        validated_data["logged_by"] = request.user.pk
        return super().create(validated_data)


class PatientAppointmentSerializer(serializers.ModelSerializer):
    """
    Appoinment Serializer for patients
    """

    patient_data = PatientSerializer(source="patient", read_only=True)
    doctor_data = PatientSerializer(source="assigned_to", read_only=True)
    logged_by = serializers.PrimaryKeyRelatedField(read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Appointment
        exclude = ("approved",)

    def validate(self, attrs):
        if self.instance:  # If update
            request = self.context["request"]
            if self.instance.logged_by != request.user.pk:
                return serializers.ValidationError(
                    {"UNAUTHORIZED": "Only the creator of the Appointment can edit it"}
                )
        return attrs

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["logged_by"] = request.user.pk
        return super().create(validated_data)
