class Menu:
    def __init__(self) -> None:
        self.options = {
            1: "Zakoduj",
            2: "Odkoduj",
            3: "Zapisz",
            4: "Pokaz Buffera",
            5: "Wyczysc buffer",
            6: "Zaladuj z pliku do buffera",
            0: "Wyjscie"
        }

    def show_menu(self) -> None:
        print("===MENU===")
        for key, value in self.options.items():
            print(f"{key}: {value}")

