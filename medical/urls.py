from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"medical_exam", MedicalExamViewSet)
router.register(r"medical_record", MedicalRecordViewSet)

urlpatterns = [
    path("api-medical/", include(router.urls)),
]