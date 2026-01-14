from .rotCipher import RotCipher

class Rot47(RotCipher):
    def encode(self, text: str) -> str:
        result = []

        for char in text:
            ascii_val = ord(char)

            if 33 <= ascii_val <= 126:
                rotated = ((ascii_val - 33 + 47) % 94) + 33
                result.append(chr(rotated))
            else:
                result.append(char)

        return ''.join(result)

    def decode(self, text: str) -> str:

        return self.encode(text)