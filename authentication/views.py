from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .serializers import *
from .models import *


class PatientViewSet(viewsets.ModelViewSet):
    """
    Patient ModelViewSet:
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class UserViewSet(viewsets.ModelViewSet):
    """
    User ModelViewSet:
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
