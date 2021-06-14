from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
User = get_user_model()

ADMIN_EMAIL = "e-clinic@esi-sba.dz"
ADMIN_PASSWORD = "admin"


def create_admins(user, username, email, password):
    try:
        user.objects.get(email=email)
        print("User " + username + " already exist")
    except User.DoesNotExist:
        u = User.objects.create_superuser(username, email, password)
        print("User " + username + " created with default password")


create_admins(User, "admin", ADMIN_EMAIL, ADMIN_PASSWORD)
