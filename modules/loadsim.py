import socket
import time
from modules.base import NetworkTool

class LoadSimulator(NetworkTool):
    """
    Limitowany test połączeń TCP – CELOWO LIMITOWANY.
    To nie jest narzędzie do zalewania serwera, tylko mały test stabilności/osiągalności.
    """

    MAX_ATTEMPTS = 200

    def __init__(self, target_ip, target_port, attempts=20):
        super().__init__(target_ip)
        self.port = int(target_port)
        n = int(attempts) if int(attempts) > 0 else 1
        self.attempts = min(n, self.MAX_ATTEMPTS)

    def execute(self):
        print(f"Limitowany test TCP na {self.target}:{self.port}, próby: {self.attempts} (max {self.MAX_ATTEMPTS})")
        success = 0
        for i in range(1, self.attempts + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                res = sock.connect_ex((self.target, self.port))
                if res == 0:
                    success += 1
                sock.close()
            except Exception:
                pass
            time.sleep(0.01)
            if i % 10 == 0 or i == self.attempts:
                print(f"Wykonano {i}/{self.attempts} prób.", end="\r")
        print()
        print(f"Zakończono. Udane połączenia: {success}/{self.attempts}.")
