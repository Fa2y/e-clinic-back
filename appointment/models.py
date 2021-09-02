from django.db import models
import uuid
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from authentication.models import *


class Appointment(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    STATUSES = (
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    logged_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    date = models.DateTimeField()
    comment = models.CharField(blank=True, null=True, max_length=255)
    assigned_to = models.ForeignKey(
        User, related_name="doctor_assigned", on_delete=models.CASCADE,null=True,blank=True
    )
    logged_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUSES, default="new", max_length=15)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return "for {} by Dr {}".format(self.patient, self.assigned_to)
