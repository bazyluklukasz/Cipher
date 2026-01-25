import json
from json import JSONDecodeError
from sqlite3 import DataError

from src.text_model import TextModel


class FileHandler:
    def save_all(self, objects: list[TextModel]):
        file_name = input("Podaj nazwe pliku: ")
        try:
            data = {"data": [obj.to_dict() for obj in objects]}
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(e)




    def load_json(self):
        file_name = input("Podaj pliku do wczytania: ")
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                result = [TextModel(**item) for item in data['data']]
                print("Wczytano Plik")
                return result
        except JSONDecodeError as e:
            print(e) # raise e
            return []
        except FileNotFoundError as e:
            print(e)
            return []




    def append_json(self, objects: list[TextModel]) :
        file_name = input("Podaj nazwe pliku do dodania: ")
        try:
            with open(file_name, "r") as file:
                existing_data: list[dict[str, str]] = json.load(file)['data']
        except FileNotFoundError as e:
            print(e)
            existing_data = []

        data = existing_data + [obj.to_dict() for obj in objects]

        try:
            with open(file_name, "w") as file:
                data_to_save = {'data': data}
                json.dump(data_to_save, file, indent=4)
        except Exception as e:
            print(e)



