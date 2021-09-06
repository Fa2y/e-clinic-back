import os
from django.core.management import call_command
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.dev")
APPS = ["authentication", "medical", "appointment"]


def install():
    import subprocess

    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])


def setup():
    django.setup()
    call_command("makemigrations", *APPS)
    call_command("migrate", interactive=False)
    call_command("loaddata", "data.json")
    call_command("runserver")


install()
setup()

# To Dump data
# python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > data.json
