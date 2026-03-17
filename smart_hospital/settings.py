from pathlib import Path
import os
from decouple import config, Csv

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# SECURITY SETTINGS
# =========================
SECRET_KEY = config("DJANGO_SECRET_KEY", default="change-me-for-prod")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [".onrender.com", "127.0.0.1", "localhost"]

# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local Apps
    "accounts",
    "hospital",

    # Third-party
    "widget_tweaks",
]

# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ✅ for static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# =========================
# URLS & WSGI
# =========================
ROOT_URLCONF = "smart_hospital.urls"

WSGI_APPLICATION = "smart_hospital.wsgi.application"

# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# =========================
# DATABASE (SQLite for now)
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =========================
# CUSTOM USER MODEL
# =========================
AUTH_USER_MODEL = "accounts.User"

# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =========================
# STATIC FILES
# =========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]   # local static
STATIC_ROOT = BASE_DIR / "staticfiles"     # collected static (Render)

# WhiteNoise static storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =========================
# MEDIA FILES
# =========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# DEFAULT AUTO FIELD
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# SECURITY (PRODUCTION)
# =========================
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

CSRF_TRUSTED_ORIGINS = [
    "https://smart-hospital-4niq.onrender.com"
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
