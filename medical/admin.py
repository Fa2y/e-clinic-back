from django.contrib import admin
from .models import MedicalExam, MedicalRecord

# Register your models here.
admin.site.register(MedicalExam)
admin.site.register(MedicalRecord) 