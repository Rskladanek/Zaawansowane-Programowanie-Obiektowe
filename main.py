"""
Główne wywołanie programu - menu i obsługa wyboru użytkownika.
"""
from modules.menu import Menu
from modules.portscanner import PortScanner
from modules.trafficgen import TrafficGenerator
from modules.loadsim import LoadSimulator
from modules.sniffer import PacketSniffer

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

        target_ip = input("Podaj adres IP celu: ").strip()
        if target_ip == "":
            if choice != 4:
                print("Adres IP nie może być pusty.")
                continue
            # For packet capture, allow empty (capture all traffic)
            target_ip = None

        if choice == 1:
            # Port scanner
            scan_type = input("Wybierz typ skanowania: (1) TCP, (2) UDP, (3) Oba: ").strip()
            if scan_type not in ["1", "2", "3"]:
                print("Nieprawidłowy wybór typu skanowania.")
                continue
            start_port_str = input("Podaj port początkowy [domyślnie 1]: ").strip()
            end_port_str = input("Podaj port końcowy [domyślnie 1024]: ").strip()
            try:
                start_port = int(start_port_str) if start_port_str != "" else 1
                end_port = int(end_port_str) if end_port_str != "" else 1024
            except ValueError:
                print("Zakres portów musi być liczbami całkowitymi.")
                continue
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                print("Nieprawidłowy zakres portów.")
                continue
            scanner = PortScanner(target_ip)
            if scan_type == "1":
                scanner.tcp_scan(start_port, end_port)
            elif scan_type == "2":
                scanner.udp_scan(start_port, end_port)
            elif scan_type == "3":
                scanner.tcp_scan(start_port, end_port)
                scanner.udp_scan(start_port, end_port)

        elif choice == 2:
            # Traffic generator (limitowany - diagnostyka)
            port_str = input("Podaj port docelowy: ").strip()
            num_str = input("Podaj liczbę pakietów [domyślnie 10, max 200]: ").strip()
            try:
                port = int(port_str)
            except ValueError:
                print("Port musi być liczbą.")
                continue
            if port < 1 or port > 65535:
                print("Nieprawidłowy numer portu.")
                continue
            try:
                num = int(num_str) if num_str != "" else 10
            except ValueError:
                print("Liczba pakietów musi być liczbą całkowitą.")
                continue
            gen = TrafficGenerator(target_ip, port, num)
            gen.execute()

        elif choice == 3:
            # Load simulation (limitowana - diagnostyka)
            port_str = input("Podaj port docelowy: ").strip()
            num_str = input("Podaj liczbę prób połączeń [domyślnie 20, max 200]: ").strip()
            try:
                port = int(port_str)
            except ValueError:
                print("Port musi być liczbą.")
                continue
            if port < 1 or port > 65535:
                print("Nieprawidłowy numer portu.")
                continue
            try:
                num = int(num_str) if num_str != "" else 20
            except ValueError:
                print("Liczba prób musi być liczbą całkowitą.")
                continue
            load = LoadSimulator(target_ip, port, num)
            load.execute()

        elif choice == 4:
            # Packet capture
            pkt_num_str = input("Podaj liczbę pakietów do przechwycenia [domyślnie 10]: ").strip()
            timeout_str = input("Podaj maksymalny czas przechwytywania (sekundy) [domyślnie 10]: ").strip()
            try:
                pkt_num = int(pkt_num_str) if pkt_num_str != "" else 10
            except ValueError:
                print("Liczba pakietów musi być liczbą całkowitą.")
                continue
            try:
                timeout = int(timeout_str) if timeout_str != "" else 10
            except ValueError:
                print("Czas musi być liczbą.")
                continue
            sniffer = PacketSniffer(target_ip, pkt_num, timeout)
            sniffer.execute()