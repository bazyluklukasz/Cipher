from src.buffer import Buffer
from src.cipher.factory_cipher import FactoryCipher
from src.file_handler import FileHandler
from src.menu import Menu
from src.menager import Manager


def main():
    menu = Menu()
    factory_cipher = FactoryCipher()
    file_handler = FileHandler()
    buffer = Buffer()
    mg = Manager(menu, factory_cipher, file_handler, buffer)
    mg.start()


if __name__ == '__main__':
    main()
