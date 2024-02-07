import os

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", 5432),
        "OPTIONS": {"options": "-c search_path=public,content"},
    }
}

include(
    "database.py",
)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
