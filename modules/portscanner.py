import socket
from modules.base import NetworkTool

"""
Wrzuciłem swój skaner portów, który wymaga przerobienia – zastosowałem dziedziczenie po klasie bazowej, w której
było potrzebne IP i port do ataku, a my będziemy chcieli jakoś to fajniej i bardziej przerobić ;)
"""

class PortScanner(NetworkTool):

    def __init__(self, target_ip, timeout=2):
        super().__init__(target_ip)
        self.timeout = timeout
        self._open_ports = {'TCP': [], 'UDP': []}

    def tcp_scan(self, start_port=1, end_port=1024):
        total_ports = end_port - start_port + 1
        scanned_ports = 0
        print(f"Rozpoczynanie skanowania TCP na {self.target}, od portu {start_port} do {end_port}...")
        for port in range(start_port, end_port + 1):
            scanned_ports += 1
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    self._open_ports['TCP'].append(port)
            print(f"Scanned {scanned_ports}/{total_ports} TCP ports.", end="\r")
        print("\nSkanowanie TCP zakończone.")
        if self._open_ports['TCP']:
            print(f"Otwarte porty TCP: {self._open_ports['TCP']}")
        else:
            print("Nie znaleziono otwartych portów TCP.")

    def udp_scan(self, start_port=1, end_port=1024):
        # Uwaga: UDP skanowanie jest heurystyczne; tu celowo limitowany timeout i brak agresywnego floodu.
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535, and start_port <= end_port.")
            return

        total_ports = end_port - start_port + 1
        scanned_ports = 0
        print(f"Rozpoczynanie skanowania UDP na {self.target}, od portu {start_port} do {end_port}...")

        for port in range(start_port, end_port + 1):
            scanned_ports += 1
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(0.1)  
                try:
                    sock.sendto(b'ping', (self.target, port))
                    try:
                        data, _ = sock.recvfrom(1024)
                        # If any data received, consider port open (service responded)
                        self._open_ports['UDP'].append(port)
                    except socket.timeout:
                        pass
                except Exception as e:
                    print(f"Błąd skanowania portu {port}: {e}")
            print(f"Scanned {scanned_ports}/{total_ports} UDP ports.", end="\r")

        print("\nSkanowanie UDP zakończone.")
        if self._open_ports['UDP']:
            print(f"Otwarte porty UDP (otrzymano odpowiedź): {self._open_ports['UDP']}")
        else:
            print("Nie znaleziono otwartych portów UDP (brak odpowiedzi).")

    def execute(self):
        print("Uruchamianie pełnego skanowania TCP i UDP (domyślnie porty 1-1024)...")
        self.tcp_scan(1, 1024)
        self.udp_scan(1, 1024)

    @property
    def open_ports(self):
        return self._open_ports
