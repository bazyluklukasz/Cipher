from src.text_model import TextModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.buffer import Buffer
    from src.file_handler import FileHandler
    from src.menu import Menu
    from src.cipher.factory_cipher import FactoryCipher



class Manager:
    def __init__(self, menu: 'Menu', factory_cipher: 'FactoryCipher', file_handler: 'FileHandler', buffer: 'Buffer'):
        self.menu = menu
        self.factory_cipher = factory_cipher
        self.file_handler = file_handler
        self.buffer = buffer

        self.options = {
            1: self.encode,
            2: self.uncode,
            3: self.save,
            4: self.show_buffer,
            5: self.clear,
            6: self.load_buffer,
            0: self.exit,
        }

    def encode(self) -> None:
        while True:
            choice_cipher = input("Jaki rot rot13 czy rot47? : ")
            if choice_cipher in self.factory_cipher.AVAILABLE_ROT_CIPHERS:
                break
            print("Blad!!!!, mozesz wybrac rot13 albo rot47")

        cip = self.factory_cipher.create_cipher(choice_cipher)
        user_text = input("Podaj text do kodowania: ")
        encode_text = cip.encode(user_text)

        self.buffer.add(TextModel(text=encode_text, rot_type=choice_cipher, status="encrypted"))

        print("Pomyslnie dodano do buffera")


    def uncode(self) -> None:
        while True:
            rot_type = input("Jaki rot: rot13 czy rot47: ")
            if rot_type in ['rot13', 'rot47']:
                break
            print("Blad!!!!, mozesz wybrac rot13 albo rot47")
        cip = self.factory_cipher.create_cipher(f"{rot_type}")
        user_text = input("Podaj text do odkodowania: ")
        decode_text = cip.decode(user_text)
        self.buffer.add(TextModel(text=decode_text, rot_type=f"{rot_type}", status="decrypted"))
        print("Pomyslnie dodano do buffera")

    def save(self) -> None:
        user_choice = int(input("\n1.Zapisac  \n2.Dodac do pliku? \nCo chcesz zrobic: "))
        if user_choice == 1:
            self.file_handler.save_all(self.buffer.data)
            print("Zapisano do pliku.")
        elif user_choice == 2:
            self.file_handler.append_json(self.buffer.data)
            print('Dodano do pliku.')
        else:
            print("Niepoprawne, powrót do menu głównego.")

    def show_buffer(self) -> None:
        self.buffer.show()

    def clear(self) -> None:
        self.buffer.clear()

    def load_buffer(self) -> None:
        self.buffer.add_multiple(self.file_handler.load_json())
        print("Zapisano do buffera.")

    def exit(self) -> None:
        exit()

    def start(self) -> None:
        try:
            while True:

                self.menu.show_menu()
                user_input = int(input("Co chcesz zrobic ?:"))
                if user_input in self.options:
                    self.options[user_input]()

        except ValueError:
            print("Blad Aplikacji")
