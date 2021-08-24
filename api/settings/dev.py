"""Use this for development"""

from .base import *

ALLOWED_HOSTS += ["127.0.0.1", "localhost", "33a2-105-235-139-78.ngrok.io"]
DEBUG = True

WSGI_APPLICATION = "api.wsgi.dev.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)
