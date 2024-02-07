import os

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY", default="django-insecure-r1j62i9xuhy@_u+1i6h6c3tg*!lp53ns@6w2-n0od0a$d)9c9p"
)

DEBUG = str(os.getenv("DJANGO_DEBUG", "FALSE")) == "1"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

include(
    "env_vars.py",
)
