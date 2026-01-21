import pytest

from cipher.factoryCipher import FactoryCipher
from cipher.rot13 import Rot13
from cipher.rot47 import Rot47


class TestFactoryCipher:

    def test_rot13(self):
        create = FactoryCipher()
        result = create.create_cipher("rot13")

        assert isinstance(result, Rot13)

    def test_rot47(self):
        create = FactoryCipher()
        result = create.create_cipher("rot47")

        assert isinstance(result, Rot47)

    def test_raise_error(self):
        create = FactoryCipher()

        with pytest.raises(ValueError):
            create.create_cipher("nothing")
