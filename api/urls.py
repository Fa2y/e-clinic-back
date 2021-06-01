from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from auth.urls import urlpatterns as authUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authUrls),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
