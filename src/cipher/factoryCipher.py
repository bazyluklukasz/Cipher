from .rot13 import Rot13
from .rot47 import Rot47
from .rotCipher import RotCipher

class FactoryCipher:
    AVAILABLE_ROT_CIPHERS = ['rot13', 'rot47']

    @staticmethod
    def create_cipher(rot_cipher : str) -> RotCipher:
        rot_cipher = rot_cipher.lower()

        if rot_cipher == "rot13":
            return Rot13()
        elif rot_cipher == "rot47":
            return Rot47()
        else:
            raise ValueError("Nie ma takiego typu rot")