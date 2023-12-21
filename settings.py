import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d+&c$tjf#&^!w($emlux#3b@=cj2^ukz$c=rhp=ysmp!1c05_e"


# Application definition

INSTALLED_APPS = [
    "db",
]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ZNO2020_CLEARED",
        "USER": "postgres",
        "PASSWORD": "6667",
        "HOST": "localhost",
        "PORT": '5432',
    }
}


USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
