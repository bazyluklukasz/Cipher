import pytest

from src.cipher.rot13 import Rot13


class TestRot13:
    test_cases = [
        ("hello world", "uryyb jbeyq"),
        ("HELLO", "URYYB"),
        ("Hello123!", "Uryyb123!"),
        ("", "")
    ]

    @pytest.mark.parametrize("text, encode", test_cases)
    def test_encode(self, text, encode,):
        ro13 = Rot13()
        assert ro13.encode(text) == encode


    @pytest.mark.parametrize("text, encode", test_cases)
    def test_decode(self, text, encode,):
        ro13 = Rot13()
        assert ro13.decode(encode) == text


    @pytest.mark.parametrize("text, encode", test_cases)
    def test_symetric(self, text, encode,):
        ro13 = Rot13()
        encod = ro13.encode(text)
        decoded = ro13.decode(encod)

        assert decoded == text