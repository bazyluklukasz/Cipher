import codecs
from .rot_cipher import RotCipher

class Rot13(RotCipher):

    def encode(self, text: str) -> str:
        return codecs.encode(text, "rot13")

    def decode(self, text: str) -> str:
        return codecs.decode(text, "rot13")