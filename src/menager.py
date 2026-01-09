import os
from time import sleep

from src import cipher
from src.buffer import Buffer
from src.menu import Menu
from src.file_handler import FileHandler
from src.cipher.FactoryCipher import FactoryCipher
from src.textModel import TextModel


class Menager:
    def __init__(self):
        self.menu = Menu()
        self.cipher = FactoryCipher()
        self.file_handler = FileHandler()
        self.cipher = FactoryCipher()
        self.buffer = Buffer()

        self.options = {
            1: self.encode,
            2: self.uncode,
            3: self.save,
            4: self.show_buffer,
            5: self.clear,
            0: self.exit,
        }

    def encode(self):
        while True:
            choice_cipher = input("Jaki rot rot13 czy rot47? : ")
            if choice_cipher in ['rot13', 'rot47']:
                break
            print("Blad!!!!, mozesz wybrac rot13 albo rot47")
        cip = self.cipher.create_cipher(f"{choice_cipher}")
        user_text = input("Podaj text do kodowania: ")
        encode_text = cip.encode(user_text)
        self.buffer.add(TextModel(text=encode_text, rot_type=f"{choice_cipher}", status="encrypted"))
        print("Pomyslnie dodano do buffera")


    def uncode(self):
        while True:
            rot_type = input("Jaki rot: rot13 czy rot47: ")
            if rot_type in ['rot13', 'rot47']:
                break
            print("Blad!!!!, mozesz wybrac rot13 albo rot47")
        cip = self.cipher.create_cipher(f"{rot_type}")
        user_text = input("Podaj text do odkodowania: ")
        decode_text = cip.decode(user_text)
        self.buffer.add(TextModel(text=decode_text, rot_type=f"{rot_type}", status="decrypted"))
        print("Pomyslnie dodano do buffera")

    def save(self):
        user_chocie = int(input("\n1.Zapisac  \n2.Dodac do pliku? \nCo chcesz zrobic: "))
        if user_chocie == 1:
            self.file_handler.save_all(self.buffer.data)
            print("Zapisano do pliku")
        elif user_chocie == 2:
            for obj in self.buffer.data:
                self.file_handler.append_json(obj)
                print("Dodano do pliku")
        else:
            print("Niepoprawne")

    def show_buffer(self):
        self.buffer.show()

    def clear(self):
        self.buffer.clear()

    def exit(self):
        exit()

    def start(self):
        try:
            while True:

                self.menu.show_menu()
                user_input = int(input("Co chcesz zrobic ?:"))
                if user_input in self.options:
                    self.options[user_input]()

        except ValueError:
            print("Blad Aplikacji")
