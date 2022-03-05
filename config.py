import os

UPLOAD_DESTINATION = os.environ.get("UPLOAD_DESTINATION")
UPLOAD_PATH = f'{os.getcwd()}{UPLOAD_DESTINATION}'

ORIGINS = [
    "*"
]

API_KEY = os.environ.get("API_KEY") or  "abc"