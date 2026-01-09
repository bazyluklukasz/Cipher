from src.textModel import TextModel


class Buffer:
    def __init__(self):
        self.data = []


    def add(self, text : TextModel):
        self.data.append(text)
        print("Dodano do buffera")

    def show(self):
        for idx, ele in enumerate(self.data):
            print(f'index : {idx}, elementy: {ele}')

    def clear(self):
        self.data.clear()
        print("Buffer zostal wyczyszczony")



