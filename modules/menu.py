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
    ║ 2) Generator ruchu (diagnostyka) — limitowane              ║
    ║ 3) Symulacje obciążeniowe        — limitowane              ║
    ║ 4) Przechwytywanie pakietów (pcap) — zapis / analiza       ║
    ║ 5) Wyjście                                                 ║
    ╠════════════════════════════════════════════════════════════╣
    ║ Uwaga: Używaj tylko na hostach/sieciach, na które masz     ║
    ║ uprawnienia. Moduły 2/3 są celowo limitowane.              ║
    ╚════════════════════════════════════════════════════════════╝
    """)


if __name__== "__main__":
    # Przykładowe wyświetlenie menu (testowe, gdy plik uruchomiony bezpośrednio)
    a = Menu()
    a.displaymenu()
