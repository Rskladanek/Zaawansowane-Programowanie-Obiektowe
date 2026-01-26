import socket
import time
from modules.base import NetworkTool

class TrafficGenerator(NetworkTool):
    """
    Diagnostyczny generator ruchu UDP – CELOWO LIMITOWANY.
    Służy do prostego sprawdzenia, czy datagramy wychodzą do hosta/portu.
    """

    MAX_PACKETS = 200

    def __init__(self, target_ip, target_port, packet_count=10):
        super().__init__(target_ip)
        self.port = int(target_port)
        # Ensure at least one packet, enforce safety cap
        n = int(packet_count) if int(packet_count) > 0 else 1
        self.packet_count = min(n, self.MAX_PACKETS)

    def execute(self):
        print(f"Diagnostyczne wysyłanie UDP do {self.target}:{self.port}, pakiety: {self.packet_count} (max {self.MAX_PACKETS})")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = 0
        for i in range(1, self.packet_count + 1):
            try:
                sock.sendto(b'X' * 128, (self.target, self.port))
                sent += 1
            except Exception as e:
                print(f"Błąd wysyłania pakietu {i}: {e}")
            # delikatne spowolnienie, żeby nie robić floodu
            time.sleep(0.01)
            print(f"Wysłano {i}/{self.packet_count} pakietów.", end="\r")
        sock.close()
        print(f"\nZakończono. Wysłano {sent} pakietów UDP do {self.target}:{self.port}.")
