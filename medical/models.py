import datetime
from django.db import models
from multiselectfield import MultiSelectField
from authentication.models import *
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE, SOFT_DELETE


def validate_file_extension(value):
    """
    Validator for uploaded files extenstions
    """
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".pdf", ".doc", ".docx", ".jpg", ".png", ".xlsx", ".xls"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


class ClinicalExam(SafeDeleteModel):
    """
    Clinical exam part of Medical exam
    """

    clinical_exam = models.TextField(blank=True, null=True)


class ParaclinicalExam(SafeDeleteModel):
    """
    Paraclinical exam part of Medical exam
    """

    paraclinical_exam = models.FileField(
        upload_to="docs/praclinicals/%Y/%m/%d",
        blank=True,
        validators=[validate_file_extension],
    )


class Evacuation(SafeDeleteModel):
    """
    Evacuation part of Medical exam
    """

    letter = models.TextField(blank=True, null=True)
    hospital = models.CharField(max_length=100, blank=True, null=True)


class Orientation(SafeDeleteModel):
    """
    Orientation part of Medical exam
    """

    orientation = models.TextField(blank=True, null=True)
    doctor_name = models.CharField(max_length=100, blank=True, null=True)


class MedicalCertificate(SafeDeleteModel):
    """
    Medical Certificate part of Medical exam
    """

    diagnosis = models.TextField(blank=True, null=True)
    days = models.IntegerField(default=1, blank=True, null=True)


class MedicalExam(SafeDeleteModel):
    """
    every medical exam has one owner(patient)
    """

    _safedelete_policy = SOFT_DELETE_CASCADE

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    clinical_exam = models.ForeignKey(
        ClinicalExam, on_delete=models.CASCADE, blank=True, null=True
    )
    paraclinical_exam = models.ForeignKey(
        ParaclinicalExam, on_delete=models.CASCADE, blank=True, null=True
    )
    evacuation = models.ForeignKey(
        Evacuation, on_delete=models.CASCADE, blank=True, null=True
    )
    orientation = models.ForeignKey(
        Orientation, on_delete=models.CASCADE, blank=True, null=True
    )
    medical_certificate = models.ForeignKey(
        MedicalCertificate, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"MedicalExam-Patient{self.patient.user.last_name} {self.patient.user.first_name}- date:{self.date}"


class Prescription(SafeDeleteModel):
    """
    Prescription part of Ordanance
    """

    medical_exam = models.ForeignKey(
        MedicalExam,
        related_name="prescriptions",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    medicament = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)
    nbPerDat = models.IntegerField(default=1, blank=True, null=True)
    nbUnit = models.IntegerField(default=1, blank=True, null=True)


class MedicalRecord(SafeDeleteModel):
    """
    every medical record has one owner(patient)
    """

    _safedelete_policy = SOFT_DELETE_CASCADE

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, unique=True)

    smoking = models.BooleanField(default=False, blank=True, null=True)
    chewing = models.BooleanField(default=False, blank=True, null=True)
    injection = models.BooleanField(default=False, blank=True, null=True)
    oldSmoker = models.BooleanField(default=False, blank=True, null=True)
    alcohol = models.BooleanField(default=False, blank=True, null=True)
    medication_consumption = models.BooleanField(default=False, blank=True, null=True)

    smokingNumberUnits = models.IntegerField(default=0, blank=True, null=True)
    chewingNumberUnits = models.IntegerField(default=0, blank=True, null=True)
    injectionNumbernits = models.IntegerField(default=0, blank=True, null=True)

    ageFc = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    medication = models.CharField(max_length=200, blank=True, null=True)
    familySituation = models.CharField(max_length=200, blank=True, null=True)
    bloodType = models.CharField(max_length=200, blank=True, null=True)
    social_number = models.CharField(max_length=200, blank=True, null=True)
    wieght = models.CharField(max_length=200, blank=True, null=True)
    height = models.CharField(max_length=200, blank=True, null=True)
    hearing_right = models.CharField(max_length=200, blank=True, null=True)
    hearing_left = models.CharField(max_length=200, blank=True, null=True)
    visual_acuity_with_correction_left = models.CharField(
        max_length=200, blank=True, null=True
    )
    visual_acuity_with_correction_right = models.CharField(
        max_length=200, blank=True, null=True
    )
    visual_acuity_without_correction_left = models.CharField(
        max_length=200, blank=True, null=True
    )
    visual_acuity_without_correction_right = models.CharField(
        max_length=200, blank=True, null=True
    )
    skin_state = models.CharField(max_length=200, blank=True, null=True)
    skin_exam = models.CharField(max_length=200, blank=True, null=True)
    ophtalmological_state = models.CharField(max_length=200, blank=True, null=True)
    ophtalmological_exam = models.CharField(max_length=200, blank=True, null=True)
    respiratory_state = models.CharField(max_length=200, blank=True, null=True)
    respiratory_exam = models.CharField(max_length=200, blank=True, null=True)
    cardiovascular_state = models.CharField(max_length=200, blank=True, null=True)
    cardiovascular_exam = models.CharField(max_length=200, blank=True, null=True)
    digestive_state = models.CharField(max_length=200, blank=True, null=True)
    digestive_exam = models.CharField(max_length=200, blank=True, null=True)
    aptitude = models.BooleanField(default=False)
    reason = models.CharField(max_length=200, blank=True, null=True)
    orl_state = models.CharField(max_length=200, blank=True, null=True)
    orl_exam = models.CharField(max_length=200, blank=True, null=True)
    locomotor_case = models.CharField(max_length=200, blank=True, null=True)
    locomotor_exam = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"MedicalRecord-for the patient:{self.id}-{self.patient}"
