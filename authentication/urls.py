from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"patients", PatientViewSet)
router.register(r"users", UserViewSet)
router.register(r"deleted_patients", DeletedPatientsViewSet)
urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path(
        "rest-auth/registration/",
        PatientRegisterView.as_view(),
    ),
    path("rest-auth/", include("dj_rest_auth.urls")),
    path("rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/", include(router.urls)),
]
