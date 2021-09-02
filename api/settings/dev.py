"""Use this for development"""

from .base import *

ALLOWED_HOSTS += ["127.0.0.1", "localhost", "6f400332b0c8.ngrok.io","10.0.2.2","192.168.43.157"]
DEBUG = True

WSGI_APPLICATION = "api.wsgi.dev.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)
