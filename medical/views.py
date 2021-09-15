from rest_framework import viewsets, filters, mixins, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import DoctorPermission, PatientPermission
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, NotFound
import json
from django.http import Http404
from .serializers import *
from authentication.serializers import PatientSerializer
from .models import *


class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
    Medical record ModelViewSet
    """

    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAuthenticated, DoctorPermission]
    search_fields = [
        "patient__user__first_name",
        "patient__user__last_name",
        "patient__type",
        "patient__education_level",
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class PatientNoMedicalRecordViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Patients with no medical record
    """

    queryset = Patient.objects.exclude(medicalrecord__in=MedicalRecord.objects.all())

    serializer_class = PatientSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAuthenticated, DoctorPermission]
    search_fields = [
        "user__first_name",
        "user__last_name",
        "type",
        "education_level",
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class PatientMedicalRecordAPIView(APIView):
    """
    Retrieve The medical record for the Patient requesting it
    """

    permission_classes = [IsAuthenticated, PatientPermission]

    def get_object(self, patient):
        try:
            return MedicalRecord.objects.get(patient=patient)
        except MedicalRecord.DoesNotExist:
            raise Http404

    def get(self, request):
        """
        GET : retrieve medical record for patient
        """
        patient = Patient.objects.get(user=request.user)
        medical_record = self.get_object(patient)
        serializer = MedicalRecordSerializer(medical_record)
        return Response(serializer.data)


class PatientMedicalExamAPIView(APIView):
    """
    Retrieve The medical exam for the Patient requesting it
    """

    permission_classes = [IsAuthenticated, PatientPermission]

    def get_objects(self, patient):
        try:
            return MedicalExam.objects.filter(patient=patient)
        except MedicalExam.DoesNotExist:
            raise Http404

    def get(self, request):
        """
        GET : retrieve medical exam for patient
        """
        patient = Patient.objects.get(user=request.user)
        medical_exam = self.get_objects(patient)
        serializer = MedicalExamSerializer(medical_exam, many=True)
        return Response(serializer.data)


class MedicalExamViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Medical Exam Modelviewset
    """

    queryset = MedicalExam.objects.all()
    serializer_class = MedicalExamSerializer
    permission_classes = [IsAuthenticated, DoctorPermission]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    @action(detail=True, methods=["post"])
    def create_detail(self, request, pk=None):
        """
        Create multi part of the medical exam
        """
        try:
            try:
                body = json.loads(request.body)
            except Exception:
                body = request.data
            # print(body.get("part", False))
            medExam = MedicalExam.objects.get(pk=pk)
            if body.get("part", False) == "clinical_exam":
                data = body.get("data", {})
                ce = ClinicalExam.objects.create(
                    clinical_exam=data.get("clinical_exam", "")
                )
                medExam.clinical_exam = ce
                medExam.save()
            elif body.get("part", False) == "paraclinical_exam":
                serializer = PraclinicalExamSerializer(data=request.FILES)
                serializer.is_valid(raise_exception=True)
                medExam.paraclinical_exam = serializer.save()
                medExam.save()
            elif body.get("part", False) == "evacuation":
                data = body.get("data", {})
                ev = Evacuation.objects.create(
                    letter=data.get("letter", ""), hospital=data.get("hospital", "")
                )
                medExam.evacuation = ev
                medExam.save()
            elif body.get("part", False) == "orientation":
                data = body.get("data", {})
                orient = Orientation.objects.create(
                    orientation=data.get("orientation", ""),
                    doctor_name=data.get("doctor_name", ""),
                )
                medExam.orientation = orient
                medExam.save()
            elif body.get("part", False) == "medical_certificate":
                data = body.get("data", {})
                mc = MedicalCertificate.objects.create(
                    diagnosis=data.get("diagnosis", ""),
                    days=data.get("days", 0),
                )
                medExam.medical_certificate = mc
                medExam.save()
            elif body.get("part", False) == "ordanance":
                data = body.get("data", {})
                for preData in data.get("med", []):
                    pre = Prescription.objects.create(
                        medicament=preData.get("medicament", ""),
                        duration=preData.get("duration", ""),
                        time=preData.get("time", ""),
                        nbPerDat=preData.get("nbPerDat", 0),
                        nbUnit=preData.get("nbUnit", 0),
                        medical_exam=medExam,
                    )
                    pre.save()

            return Response(
                {"details": "Added successfully to medical exam"},
                status=status.HTTP_202_ACCEPTED,
            )
        except MedicalExam.DoesNotExist:
            raise NotFound()
        # except Exception:
        #     raise ParseError()


class StatisticsAPIView(APIView):
    """
    Retrieve Multiple diffrent statistics
    """

    permission_classes = [IsAuthenticated, DoctorPermission]

    def get_smokers(self, medrecs):
        """
        Get Smokers stats
        """
        from itertools import groupby

        data = {
            key: len(list(group))
            for key, group in groupby(
                medrecs.filter(smoking=True), lambda medr: medr.patient.education_level
            )
        }
        return data

    def get_alcohol(self, medrecs):
        """
        Get Alcoholics stats
        """
        from itertools import groupby

        dataLevel = {
            key: len(list(group))
            for key, group in groupby(
                medrecs.filter(alcohol=True), lambda medr: medr.patient.education_level
            )
        }
        dataSex = {
            key: len(list(group))
            for key, group in groupby(
                medrecs.filter(alcohol=True), lambda medr: medr.patient.user.sex
            )
        }
        return {"level": dataLevel, "sex": dataSex}

    def get(self, request):
        """
        GET : Statistics
        """
        medrecs = MedicalRecord.objects.all()
        smokers = self.get_smokers(medrecs)
        alcoholics = self.get_alcohol(medrecs)
        data = {"smokers": smokers, "alcoholics": alcoholics, "all": medrecs.count()}
        return Response(data)
