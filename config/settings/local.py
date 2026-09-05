from .base import *

DEBUG = True
SECRET_KEY = getenv("SECRET_KEY", "codespaces-development-secret-key")
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]
ADMIN_URL = getenv("ADMIN_URL", "admin/")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
