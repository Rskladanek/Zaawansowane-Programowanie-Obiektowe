class Menu():
    """
    baza sterująca wszystkimi operacjami i klasami – tutaj mają być importy klas z modules
    """
    def __init__(self):
        pass

    @staticmethod
    def displaymenu():
        # Wyświetlenie menu głównego z dostępnymi opcjami:
        print("""
    ╔════════════════════════════════════════════════════════════╗
    ║            Zaawansowane Programowanie Obiektowe            ║
    ║                    Network Toolkit                         ║
    ╠════════════════════════════════════════════════════════════╣
    ║ 1) Skaner portów (TCP/UDP)       — audyt własnych hostów   ║
    ║ 2) Generator ruchu (symulacja)   — tylko lab / sandbox     ║
    ║ 3) Symulacje obciążeniowe        — kontrolowane testy      ║
    ║ 4) Przechwytywanie pakietów (pcap) — zapis / analiza       ║
    ║ 5) Wyjście                                                 ║
    ╠════════════════════════════════════════════════════════════╣
    ║ Uwaga: Wszystkie operacje uruchamiaj tylko w środowisku    ║
    ║ testowym lub na systemach, na które masz pisemną zgodę.    ║
    ╚════════════════════════════════════════════════════════════╝
    """)


if __name__== "__main__":
    # Przykładowe wyświetlenie menu (testowe, gdy plik uruchomiony bezpośrednio)
    a = Menu()
    a.displaymenu()
