from src.cipher.rotCipher import RotCipher


class DummyRotCipher(RotCipher):

    def encode(self, text: str) -> str:
        return text

    def decode(self, text: str) -> str:
        return text


class TestRotCipher:

    def test_encode(self):
        cipher = DummyRotCipher()

        assert cipher.encode("hello") == "hello"
        assert cipher.decode("hello") == "hello"
