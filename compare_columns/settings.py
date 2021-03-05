from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = int(os.environ.get("DEBUG", default=0))

os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
INSTALLED_APPS = ["columns", "vertical_multi_columns"]

ROOT_URLCONF = "compare_columns.urls"

WSGI_APPLICATION = 'compare_columns.wsgi.application'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "compare_columns/templates")],
    },
]

VERTICAL_MULTI_COLUMNS = [
    {"NUMBER_OF_COLUMNS": 3},
]




