from django.db import models
import datetime
from django.utils.deconstruct import deconstructible
from multiselectfield import MultiSelectField
from authentication.models import *
# Create your models here.


class MedicalExam(models.Model):
    '''
    every medical exam has one owner(patient)
    '''
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    date= models.DateField(auto_now=False, auto_now_add=False)

    doctor_name= models.CharField(max_length=100)

    wieght=models.IntegerField(max_length=2)
    height=models.IntegerField(max_length=2)

    hearing_right= models.CharField(max_length=20)
    hearing_left= models.CharField(max_length=20)

    visual_acuity_with_correction_left=models.CharField(max_length=20)
    visual_acuity_with_correction_right=models.CharField(max_length=20)
    visual_acuity_without_correction_left=models.CharField(max_length=20)
    visual_acuity_without_correction_right=models.CharField(max_length=20, default=" ")

    SKINPROBLEMS= [
        ("skin infection", "skin infection")
    ]
    skin_state= MultiSelectField(choices=SKINPROBLEMS, blank=True)
    skin_exam= models.TextField(blank=True)

    OPHTALMOLOGYPROBLEMS= [
        ("tearing", "tearing"),
        ("pain", "pain"),
        ("eye spots", "eye spots"),

    ]
    ophtalmological_state= MultiSelectField(choices=OPHTALMOLOGYPROBLEMS, blank=True)
    ophtalmological_exam = models.TextField(blank=True)

    ORLPROBLEMS = [
        ("whistling", "whistling"),
        ("repeated tonsillitis", "repeated tonsillitis"),
        ("epistaxis", "epistaxis"),
        ("rhinorrhea", "rhinorrhea"),
    ]
    orl_state=  MultiSelectField(choices=ORLPROBLEMS, blank=True)
    orl_exam=  models.TextField(blank=True)

    LOCOMOTORPROLEMS= [
        ("muscular", "muscular"),
        ("articular", "articular"),
        ("vertebral", "vertebral"),
        ("neurological", "neurological"),
    ]
    locomotor_case= MultiSelectField(choices=LOCOMOTORPROLEMS, blank=True)
    locomotor_exam=  models.TextField(blank=True)

    RESPIRATORYPROBLEMS = [
        ("cough", "cough"),
        ("dyspnea", "dyspnea"),
        ("expectoration", "expectoration"),
        ("chest pain", "chest pain"),
    ]
    respiratory_state= MultiSelectField(choices=RESPIRATORYPROBLEMS, blank=True)
    respiratory_exam=  models.TextField(blank=True)

    CARDIOVASCULARPROBLEMS = [
        ("palpitations","palpitations"),
        ("edema pain","edema pain"),
        ("pain on walk", "pain on walk"),
        ("pain on rest", "pain on rest"),
        ("pain on effort", "pain on effort"),
    ]
    cardiovascular_state= MultiSelectField(choices=CARDIOVASCULARPROBLEMS,  blank=True)
    cardiovascular_exam=  models.TextField(blank=True)

    DIGESTIVEPROBLEMS = [
        ("appetite problem", "appetite problem" ),
        ("transit", "transit"),
        ("stool", "stool"),
        ("rectal bleeding", "rectal bleeding"),
        ("abdominal pain", "abdominal pain"),
    ]
    digestive_state= MultiSelectField(choices=DIGESTIVEPROBLEMS, blank=True)
    digestive_exam=  models.TextField(blank=True)


    aptitude=models.BooleanField(default=False) #apt=True inapt=False the default is inapt
    reason=models.TextField(blank=False)

    #orientation
    orientation_specialist=models.CharField(max_length=100, blank=True)
     
    CAUSES = [
        ("notice", "notice"),
        ("hospitalization", "hospitalization"),
        ("treatment", "treatment"),
     ]

    orientation_cause= models.CharField(max_length=50, choices=CAUSES, default="notice", blank=True)

    orientation_response= models.TextField(blank=True)

    
    def __str__(self):
        return f"MedicalExam-doctor:{self.doctor_name}-Patient{self.patient.user.last_name} {self.patient.user.first_name}date:{self.date}"





class MedicalRecord(models.Model):
    '''
    every medical record has one owner(patient)
    '''
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE ,unique=True )

    social_number= models.BigIntegerField(unique=True)
    biometric= models.CharField(max_length=200, unique=True)

    tobaco_consumption=models.BooleanField(default=False)
    PRODUCT = [
        ("smoking tobaco", "smoking tobaco"),
        ("chewing tobaco", "chewing tobaco"),
        ("injection tobaco", "injection tobaco"),
    ]

    tobaco_taken_as=models.CharField(max_length=50, choices=PRODUCT, blank=True)
    number_units=models.IntegerField(max_length=2, blank=True, null=True)

    alcohol_consumption = models.BooleanField(default=False)
    
    medication_consumption = models.BooleanField(default=False) 
    medications=models.TextField(blank=True)

    other = models.TextField(blank=True)

    general_diseases=models.TextField(blank=True)
    surgical_intervention=models.TextField(blank=True)
    congenital_condition=models.TextField(blank=True)
    allergic_reaction=models.TextField(blank=True)
    
    #every medical record can include many medical exams
    screening = models.ForeignKey(MedicalExam, on_delete=models.CASCADE) 


    def __str__(self):
        return f"MedicalRecord-for the patient:{self.biometric}-{self.patient.user.last_name} {self.patient.user.first_name}"

