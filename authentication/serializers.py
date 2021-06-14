from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    '''
    User Model Serializer
    Excluded Fields: password, username, is_staff, user_permissions, groups
    '''
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        exclude = ('username', 'is_staff',
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
        user_data = validated_data.pop('user')
        user = User.objects.create(email=user_data.get('email'))
        user.set_password(user_data.get('password'))
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
        return attrs
