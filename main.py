"""
Tutaj będzie menu do naszego program baza sterująca wszystkimi operacjami i klasami
"""
from modules.menu import Menu
from modules.portscanner import PortScanner


if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.displaymenu()
        try:
            choice = int(input("Wybierz opcję (1-5): "))
        except ValueError:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            continue

        if choice == 5:
            print("Koniec programu.")
            break

        if choice not in [1, 2, 3, 4]:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            continue

### Tutaj będzie kontrnuacja potem wrzuce