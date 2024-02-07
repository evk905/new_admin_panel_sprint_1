from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = "config.urls"

INTERNAL_IPS = [
    "127.0.0.1",
]

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

include("components/env_vars.py")
include("components/applications.py")
include("components/database.py")
include("components/auth_password_validators.py")
include("components/statics.py")

LOCALE_PATHS = ["movies/locale"]
