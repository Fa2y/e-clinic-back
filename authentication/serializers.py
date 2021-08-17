from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from .models import *


class UserSerializer(serializers.ModelSerializer):
    """
    User Model Serializer
    Excluded Fields: password, username, is_staff, user_permissions, groups
    """

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            "username",
            "password",
            "is_staff",
            "user_permissions",
            "groups",
        )


class PatientSerializer(serializers.ModelSerializer):
    """
    Patient Model Serializer
    Excluded Fields: is_approved(default=False)
    """

    user = UserSerializer()

    class Meta:
        model = Patient
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(email=user_data.get("email"))
        email_addr = EmailAddress.objects.create(
            user=user, email=user_data.get("email")
        )
        request = self.context["request"]
        email_addr.send_confirmation(request, True)
        password = get_adapter().clean_password(user_data.get("password1"))
        user.set_password(password)
        user.first_name = user_data.get("first_name", "")
        user.last_name = user_data.get("last_name", "")
        user.sex = user_data.get("sex", "Male")
        user.role = "Patient"
        user.image = user_data.get("image", None)
        user.phone = user_data.get("phone", "")
        user.data_of_birth = user_data.get("data_of_birth", "")
        user.city = user_data.get("city", "")
        user.address = user_data.get("address", "")
        user.save()
        instance = Patient.objects.create(user=user)
        if validated_data.get("is_approved", False):
            validated_data.pop("is_approved")
        instance = super().update(instance, validated_data)
        instance.save()
        return instance

    def validate(self, attrs):
        user_data = attrs.get("user", False)
        if not user_data:
            return attrs
        if user_data["password1"] != user_data["password2"]:
            raise serializers.ValidationError(
                _("The two password fields didn't match.")
            )

        if attrs.get("type") == "ATP" and attrs.get("education_level") != "NONE":
            raise serializers.ValidationError(_("ATP's education level must be NONE!"))

        if attrs.get("type") == "Student" and attrs.get("education_level") not in [
            "1CPI",
            "2CPI",
            "1CS",
            "2CS-ISI",
            "2CS-SIW",
            "3CS-ISI",
            "3CS-SIW",
        ]:
            raise serializers.ValidationError(_("invalid education level for student"))

        if attrs.get("type") == "Teacher" and attrs.get("education_level") not in [
            "MA-A",
            "MA-B",
            "MC-A",
            "MC-B",
            "Professor",
        ]:
            raise serializers.ValidationError(_("invalid education level for Teacher"))
        return attrs

    def save(self, request):
        print(request)
        return super().save()


class PatientProfileSerializer(serializers.ModelSerializer):
    """
    Patient Model Serializer
    Excluded Fields: is_approved(default=False)
    """

    class Meta:
        model = Patient
        exclude = ("user",)


class UserProfileSerializer(UserDetailsSerializer):
    patient = PatientProfileSerializer()

    class Meta(UserSerializer.Meta):
        pass
