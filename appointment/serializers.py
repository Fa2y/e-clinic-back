from rest_framework import serializers
from authentication.models import Patient, User
from .models import Appointment
from .notification_push import push_notify


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
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    logged_by = UserSerializer(read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        validated_data["approved"] = True
        request = self.context["request"]
        validated_data["logged_by"] = request.user
        validated_data["assigned_to"] = request.user
        title = "New Appointment"
        body = f"New appointment was assigned to you by Dr.{request.user.last_name} {request.user.first_name}"
        patient_uid = validated_data.get("patient", None).user.uid
        push_notify(patient_uid, title, body)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context["request"]
        if validated_data.get("status", False) == "cancelled":
            title = "Appointment Cancelled"
            body = f"Your appointment request was cancelled by Dr.{request.user.last_name} {request.user.first_name}"
            patient_uid = instance.patient.user.uid
            push_notify(patient_uid, title, body)
        return super().update(instance, validated_data)


class PatientAppointmentSerializer(serializers.ModelSerializer):
    """
    Appoinment Serializer for patients
    """

    doctor_data = UserSerializer(source="assigned_to", read_only=True)
    logged_by = serializers.PrimaryKeyRelatedField(read_only=True)
    approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = Appointment
        exclude = ("patient", "assigned_to")

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
        validated_data["logged_by"] = request.user
        validated_data["assigned_to"] = User.objects.filter(role="Doctor").first()
        validated_data["patient"] = Patient.objects.get(user=request.user)
        return super().create(validated_data)
