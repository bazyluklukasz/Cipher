from src.text_model import TextModel


class Buffer:
    def __init__(self) -> None:
        self.data: list[TextModel] = []


    def add(self, text: TextModel) -> None:
        self.data.append(text)
        print("Dodano do buffera")

    def add_multiple(self, text:  list[TextModel]) -> None:
        self.data += text

    def show(self) -> bool:
        if self.data:
            for idx, ele in enumerate(self.data, start=1):
                print(f'{idx}. {ele}')
                return True

        print("Bufer jest Pusty")
        return False

    def clear(self) -> None:
        self.data.clear()
        print("Buffer zostal wyczyszczony")




