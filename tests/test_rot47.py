import pytest

from src.cipher.rot47 import Rot47


class TestRot47:
    test_cases = [
        ("Hello", "w6==@"),
        ("Hello123!", "w6==@`abP"),
        ("", ""),
        (" ~!#@#$!@#", " OPRoRSPoR"),
    ]

    @pytest.mark.parametrize("test_input,expected", test_cases)
    def test_encode(self,test_input,expected):
        rot47 = Rot47()

        assert rot47.encode(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", test_cases)
    def test_decode(self,test_input,expected):
        rot47 = Rot47()

        assert rot47.decode(expected) == test_input

    @pytest.mark.parametrize("test_input,expected", test_cases)
    def test_symetric(self,test_input,expected):
        rot47 = Rot47()
        encoded = rot47.encode(test_input)
        decoded = rot47.decode(encoded)

        assert decoded == test_input



