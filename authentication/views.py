from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .serializers import *
from .models import *


class PatientView(viewsets.ModelViewSet):
    """
        Patient APIView:
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
