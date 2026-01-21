from src.textModel import TextModel


class Buffer:
    def __init__(self):
        self.data = []


    def add(self, text: TextModel):
        self.data.append(text)
        print("Dodano do buffera")

    def show(self):
        if self.data :

            for idx, ele in enumerate(self.data, start=1):
                print(f'{idx}. {ele}')
                return True
        else:
            print("Bufer jest Pusty")
            return False

    def clear(self):
        self.data.clear()
        print("Buffer zostal wyczyszczony")




