import hashlib
import os
import random
from datetime import datetime
from uuid import uuid4


def now():
    return datetime.now()


def generate_id():
    return str(uuid4())


def generate_key():
    return uuid4().hex


def generate_otp():
    otp = ""
    while len(otp) < 6:
        otp += str(random.randint(0, 9))
    return otp


def date_time_diff_min(start: datetime, end: datetime):
    duration = end - start
    duration_in_seconds = duration.total_seconds()
    minutes = divmod(duration_in_seconds, 60)[0]
    return minutes


def remove_file(path):
    os.remove(path)


def create_hash(key: str) -> str:
    key = key.encode()
    key = hashlib.sha256(key).digest()
    key = key.decode("unicode_escape")
    return key
