import json
import os

from fastapi import HTTPException, status

DB_HOST = os.environ.get("FA_DB_HOST", "localhost")
DB_USER = os.environ.get("FA_DB_USER", "postgres")
DB_PASSWORD = os.environ.get("FA_DB_PASSWORD", "root")
DB_NAME = os.environ.get("FA_DB_NAME", "fastapi")
JWT_KEY = os.environ.get("FA_JWT_KEY", '{"k":"shynMnd8Fqy9h5X4dUza19CTi1GT38NawuJw0BJPQp4","kty":"oct"}')
FERNET_KEY = os.environ.get("FA_FERNET_KEY", "qY9lhwjxsqpBItnQVqbyiefkuS6kM9dwDM0a1zHQ7SM=")
RE_CAPTCHA_SECRET = os.environ.get("FA_RE_CAPTCHA_SECRET")
SES_FROM_EMAIL = os.environ.get("FA_SES_FROM_EMAIL")

if JWT_KEY:
    try:
        JWT_KEY = json.loads(JWT_KEY)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid JWT key"
        )
else:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="JWT key not set"
    )
