import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = <your secret key>

DEBUG = 1

ALLOWED_HOSTS = ["localhost"]

INSTALLED_APPS = ["columns", "vertical_multi_columns"]

ROOT_URLCONF = "compare_columns.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "compare_columns/templates")],
    },
]

VERTICAL_MULTI_COLUMNS = [
    {"NUMBER_OF_COLUMNS": 3},
]




