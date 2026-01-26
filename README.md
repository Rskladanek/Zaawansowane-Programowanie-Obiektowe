# Zaawansowane Programowanie Obiektowe – Network Toolkit (wersja do zaliczenia)

To jest **edukacyjny** zestaw narzędzi sieciowych uruchamianych z konsoli, przygotowany tak, żeby spełniał wymagania
projektu z ZPO: **hermetyzacja, dziedziczenie, polimorfizm** oraz sensowna struktura wielu klas.

> Uwaga: narzędzia działają wyłącznie do diagnostyki i testów na hostach/sieciach, na które masz uprawnienia.
> Moduły „trafficgen” i „loadsim” są celowo **limitowane** (nie są „flooderami”) – to testy łączności / małego obciążenia,
> a nie narzędzia do nadużyć.

## Struktura projektu
```text
Zaawansowane-Programowanie-Obiektowe/
├── README.md
├── .gitignore
├── main.py
└── modules/
    ├── base.py
    ├── menu.py
    ├── portscanner.py
    ├── trafficgen.py
    ├── loadsim.py
    └── sniffer.py
```

## Wymagania
- Python 3.10+
- (opcjonalnie) `scapy` dla sniffera

## Instalacja
```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
# .\venv\Scripts\activate

pip install -r requirements.txt
```

## Uruchomienie
```bash
python main.py
```

## OOP – jak to jest zrobione
- **Hermetyzacja:** `NetworkTool` trzyma `_target` i wystawia property `target`.
- **Dziedziczenie:** `PortScanner`, `TrafficGenerator`, `LoadSimulator`, `PacketSniffer` dziedziczą po `NetworkTool`.
- **Polimorfizm:** każda klasa implementuje `execute()`; w `main.py` wywołujesz `obj.execute()` niezależnie od typu.

## Co robią moduły
- `PortScanner`: skanuje TCP i (ograniczone) UDP w zadanym zakresie.
- `TrafficGenerator`: wysyła *limitowaną* liczbę datagramów UDP w celach diagnostycznych.
- `LoadSimulator`: wykonuje *limitowaną* serię połączeń TCP i raportuje ile się udało.
- `PacketSniffer`: przechwytuje pakiety i zapisuje do `capture.pcap` (wymaga uprawnień i scapy).
