from django.urls import path, include
from .views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path(r'api/patient', PatientView.as_view(), name="patientAPIview")
]
