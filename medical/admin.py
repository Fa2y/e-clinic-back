from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MedicalExam)
admin.site.register(ClinicalExam)
admin.site.register(ParaclinicalExam)
admin.site.register(Evacuation)
admin.site.register(Orientation)
admin.site.register(MedicalCertificate)
admin.site.register(Prescription)
admin.site.register(MedicalRecord)
