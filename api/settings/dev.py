"""Use this for development"""

from .base import *

ALLOWED_HOSTS += ["127.0.0.1", "localhost"]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:5000",
    "http://localhost:3000",
]
DEBUG = True

WSGI_APPLICATION = "api.wsgi.dev.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)
