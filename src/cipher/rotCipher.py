from abc import ABC, abstractmethod


class RotCipher(ABC):


    @abstractmethod
    def encode(self, text: str) -> str:
        pass

    @abstractmethod
    def decode(self, text: str) -> str:
        pass