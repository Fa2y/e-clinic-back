from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    '''
    User Model Serializer
    Excluded Fields: password, username, is_staff, user_permissions, groups
    '''
    class Meta:
        model = User
        exclude = ('password', 'username', 'is_staff',
                   'user_permissions', 'groups',)


class PatientSerializer(serializers.ModelSerializer):
    '''
    Patient Model Serializer
    Excluded Fields: is_approaved(default=False)
    '''
    user = UserSerializer()

    class Meta:
        model = Patient
        exclude = ('is_approaved',)

    def create(self, validated_data):
        print('CREATINNG')
        user_data = validated_data.pop('user')
        user = User.objects.create(email=user_data.get('email'))
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
        instance = super().update(instance, validated_data)
        instance.save()
        return instance

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        return instance
