from cryptography.fernet import Fernet

from app.config import FERNET_KEY


class Fernets:
    """
    This class is used to encrypt and decrypt data
    using the fernet algorithm.
    """

    def __init__(self):
        self.key = FERNET_KEY.encode()
        self.fernet = Fernet(self.key)

    def encrypt(self, data):
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, data):
        return self.fernet.decrypt(data).decode()
