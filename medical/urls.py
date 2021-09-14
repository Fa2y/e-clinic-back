from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"medical_exam", MedicalExamViewSet)
router.register(r"medical_record", MedicalRecordViewSet)
router.register(r"patient_no_medical_record", PatientNoMedicalRecordViewSet)
# router.register(
#     r"patient_medical_record",
#     PatientMedicalRecordAPIView,,
#     basename="patient_medical_record",
# )

urlpatterns = [
    path("api-medical/", include(router.urls)),
    path(
        r"api-medical/patient_medical_record/",
        PatientMedicalRecordAPIView.as_view(),
    ),
]
