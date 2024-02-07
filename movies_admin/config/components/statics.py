from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

STATIC_URL = "static/"

include(
    "statics.py",
)
