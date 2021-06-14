from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from allauth.account.adapter import get_adapter
from .models import *


class UserSerializer(serializers.ModelSerializer):
    '''
    User Model Serializer
    Excluded Fields: password, username, is_staff, user_permissions, groups
    '''
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ('username', 'password', 'is_staff',
                   'user_permissions', 'groups',)


class PatientSerializer(serializers.ModelSerializer):
    '''
    Patient Model Serializer
    Excluded Fields: is_approved(default=False)
    '''
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        print("CREATING")
        user_data = validated_data.pop('user')
        user = User.objects.create(email=user_data.get('email'))
        password = get_adapter().clean_password(user_data.get('password1'))
        user.set_password(password)
        user.first_name = user_data.get('first_name', '')
        user.last_name = user_data.get('last_name', '')
        user.sex = user_data.get('sex', 'Male')
        user.role = 'Patient'
        user.image = user_data.get('image', None)
        user.phone = user_data.get('phone', '')
        user.data_of_birth = user_data.get('data_of_birth', '')
        user.city = user_data.get('city', '')
        user.address = user_data.get('address', '')
        user.save()
        instance = Patient.objects.create(user=user)
        if validated_data.get('is_approved', False):
            validated_data.pop('is_approved')
        instance = super().update(instance, validated_data)
        instance.save()
        return instance

    def validate(self, attrs):
        print("VALIDATING")
        user_data = attrs.get('user')
        if user_data['password1'] != user_data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return attrs
