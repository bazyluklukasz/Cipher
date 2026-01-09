import json
from json import JSONDecodeError
from sqlite3 import DataError

from src.textModel import TextModel


class FileHandler:

    def save_all(self, object: list[TextModel]):
        file_name = input("Podaj nazwe pliku do nadpisania: ")
        data = []
        try:
            data = [obj.to_dict() for obj in object]
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(e)




    def load_json(self):
        file_name = input("Podaj pliku do wczytania: ")
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                result = [TextModel(**item) for item in data]
                print("Wczytano Plik")
                return result
        except JSONDecodeError as e:
            print(e)
            return []
        except FileNotFoundError as e:
            print(e)
            return []




    def append_json(self, obj: TextModel) :
        file_name = input("Podaj nazwe pliku do dodania: ")
        existing_data = []
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                existing_data =[TextModel(**item) for item in data]
        except FileNotFoundError as e:
            print(e)
            existing_data = []

        existing_data.append(obj)

        try:
            with open(file_name, "w") as file:
                data_to_save = [item.to_dict() for item in existing_data]
                json.dump(data_to_save, file, indent=4)
        except Exception as e:
            print(e)



