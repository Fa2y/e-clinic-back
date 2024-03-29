from django.contrib import admin
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "rest-auth/registration/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
    ),
    path(
        r"^rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("", include("authentication.urls")),
    path("", include("medical.urls")),
    path("", include("appointment.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
