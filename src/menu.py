class Menu:
    def __init__(self):
        self.options = {
            1: "Zakoduj",
            2: "Odkoduj",
            3: "Zapisz",
            4: "Pokaz Buffera",
            5: "Wyczysc buffer",
            0: "Wyjscie"
        }

    def show_menu(self):
        print("===MENU===")
        for key, value in self.options.items():
            print(f"{key}: {value}")

