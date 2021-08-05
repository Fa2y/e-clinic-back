from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ParseError
from dj_rest_auth.registration.views import RegisterView
from .serializers import *
from .models import *


class PatientRegisterView(RegisterView):
    serializer_class = PatientSerializer

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        return user


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


class DeletedPatientsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Deleted Patients ModelViewSet:
    """

    queryset = Patient.objects.deleted_only()
    serializer_class = PatientSerializer

    # Method to restore deleted patient
    @action(detail=True, methods=["patch"])
    def restore(self, request, pk=None):
        try:
            # Fetching instance
            patient_query = Patient.objects.deleted_only().filter(pk=pk)
            if patient_query.exists():
                instance = patient_query[0]
                instance.undelete()
                return Response(status=status.HTTP_200_OK)
            else:
                raise Patient.DoesNotExist
        except Patient.DoesNotExist:
            raise NotFound()
        except Exception:
            raise ParseError()
