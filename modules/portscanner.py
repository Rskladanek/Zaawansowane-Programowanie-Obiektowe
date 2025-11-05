import socket
from example import Inheritance

"""
Wrzuciłem swój skanner portów który wymaga przerobienia zastosowałem dziedziczenie po klasie bazowej w której
było potrzebne IP i port do ataku a my będziemy chcieli jakoś to fajniej i bardziej przerobić ;)
"""


class PortScanner(Inheritance):

    def __init__(self, ip, timeout=2):
        super().__init__(ip)
        self.timeout = timeout
        self.open_ports = {'TCP': [], 'UDP': []}

    def tcp_scan(self, start_port=0, end_port=1024):
        total_ports = end_port - start_port + 1
        scanned_ports = 0
        print(f"Starting TCP scan on {self.ip} from port {start_port} to {end_port}...")
        for port in range(start_port, end_port + 1):
            scanned_ports += 1
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.ip, port))
                if result == 0:
                    self.open_ports['TCP'].append(port)
            print(f"Scanned {scanned_ports}/{total_ports} TCP ports.", end="\r")
        print("\nTCP scan completed.")
        if self.open_ports['TCP']:
            print(f"Open TCP ports: {self.open_ports['TCP']}")
        else:
            print("No open TCP ports found.")

    def udp_scan(self, start_port=1, end_port=1024):
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535, and start_port <= end_port.")
            return

        total_ports = end_port - start_port + 1
        scanned_ports = 0
        print(f"Starting UDP scan on {self.ip} from port {start_port} to {end_port}...")

        for port in range(start_port, end_port + 1):
            scanned_ports += 1
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(0.1)  

                try:
                    sock.sendto(b'', (self.ip, port))

                    try:
                        data, _ = sock.recvfrom(1024)
                        self.open_ports['UDP'].append(port)
                    except socket.timeout:
                        pass
                except Exception as e:
                    print(f"Error scanning port {port}: {e}")

            # Update progress
            print(f"Scanned {scanned_ports}/{total_ports} UDP ports.", end="\r")

        print("\nUDP scan completed.")
        if self.open_ports['UDP']:
            print(f"Open UDP ports (responses received): {self.open_ports['UDP']}")
        else:
            print("No open UDP ports found (no responses received).")