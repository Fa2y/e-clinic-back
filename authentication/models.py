from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import datetime
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE, SOFT_DELETE


@deconstructible
class ESISBAEmailValidator(EmailValidator):
    """
    A validator that validate email format and checks for
    the domain name to include"esi-sba.dz"
    """

    message = "Only esi-sba.dz emails are accepted."

    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, ESISBAEmailValidator) and super().__eq__(other)


class User(AbstractUser, SafeDeleteModel):
    """
    Base User Model
    """

    _safedelete_policy = SOFT_DELETE

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    username = models.CharField(null=True, max_length=150)
    sex = models.CharField(max_length=200, choices=GENDER, default="Male")
    ROLES = [
        ("Admin", "Admin"),
        ("GRH", "GRH"),
        ("Doctor", "Doctor"),
        ("Nurse", "Nurse"),
        ("Patient", "Patient"),
    ]
    email = models.EmailField(
        unique=True,
        max_length=60,
        validators=[ESISBAEmailValidator(allowlist=["esi-sba.dz"])],
    )
    role = models.CharField(max_length=50, choices=ROLES, default="Patient")
    image = models.ImageField(upload_to="userImages", blank=True,null=True)
    phone = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=2, blank=True)
    address = models.CharField(max_length=200, blank=True)
    is_confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name_plural = "User"

    def __str__(self):
        return (
            str(self.uid)
            + " - "
            + self.email
            + " - "
            + self.first_name
            + " - "
            + self.last_name
        )


class Patient(SafeDeleteModel):
    """
    Patient role User, inherit from Base User
    """

    _safedelete_policy = SOFT_DELETE_CASCADE

    pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    TYPES = [("ATP", "ATP"), ("Student", "Student"), ("Teacher", "Teacher")]
    type = models.CharField(max_length=50, choices=TYPES, default="Student")
    LEVELS = [
        # in case of ATP
        ("NONE", "NONE"),
        # in case of Teacher
        ("MA-A", "MA-A"),
        ("MA-B", "MA-B"),
        ("MC-A", "MC-A"),
        ("MC-B", "MC-B"),
        ("Professor", "Professor"),
        # in case of Student
        ("1CPI", "1CPI"),
        ("2CPI", "2CPI"),
        ("1CS", "1CS"),
        ("2CS-ISI", "2CS-ISI"),
        ("2CS-SIW", "2CS-SIW"),
        ("3CS-ISI", "3CS-ISI"),
        ("3CS-SIW", "3CS-SIW"),
    ]
    education_level = models.CharField(max_length=50, choices=LEVELS, default="NONE")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Patient-{self.type}-{self.user.last_name} {self.user.first_name}"
