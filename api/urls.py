from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
    path(r'^rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
         name='account_confirm_email'),
    path("", include("authentication.urls")),
    path("", include("medical.urls")),
]
