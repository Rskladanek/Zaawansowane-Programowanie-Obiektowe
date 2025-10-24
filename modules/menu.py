class Menu():
    """
    baza sterująca wszystkimi operacjami i klasami tutaj maja być wszystkie importy klas z modules
    """
    def __init__(self):
        pass


    @staticmethod
    def displaymenu():
        # Tutaj bedzie duzo zmian taki przyklad wymyslilem
        print("""
    ╔════════════════════════════════════════════════════════════╗
    ║            ZAawansowane Programowanie Obiektowe            ║
    ║                    Network Toolkit                         ║
    ╠════════════════════════════════════════════════════════════╣
    ║ 1) Skaner portów (TCP/UDP)       — audyt własnych hostów   ║
    ║ 2) Generator ruchu (symulacja)    — tylko lab / sandbox    ║
    ║ 3) Symulacje obciążeniowe         — kontrolowane testy     ║
    ║ 4) Przechwytywanie pakietów (pcap) — zapis / analiza       ║
    ║ 5) Audyt konfiguracji serwera     — raporty i rekomendacje ║
    ║ 6) Analiza pcap (pyshark/scapy)   — przetwarzanie i filtry ║
    ║ 7) Import/eksport wyników (JSON/CSV)                       ║
    ║ 8) Ustawienia labu / topologia    — tworzenie VM i sieci   ║
    ║ 9) Pomoc / Etyka                   — zasady użycia         ║
    ║ 0) Wyjście                                                 ║
    ╠════════════════════════════════════════════════════════════╣
    ║ Uwaga: Wszystkie operacje uruchamiaj tylko w środowisku    ║
    ║ testowym lub na systemach, na które masz pisemną zgodę.    ║
    ╚════════════════════════════════════════════════════════════╝
    """)


if __name__== "__main__":
    a = Menu()
    a.displaymenu()