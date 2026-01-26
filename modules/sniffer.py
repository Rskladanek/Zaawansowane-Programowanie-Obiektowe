from modules.base import NetworkTool

class PacketSniffer(NetworkTool):
    def __init__(self, target_ip=None, packet_count=10, timeout=10):
        super().__init__(target_ip)
        self.packet_count = packet_count if packet_count > 0 else 1
        # If timeout <= 0, use None (no timeout)
        self.timeout = timeout if timeout and timeout > 0 else None

    def execute(self):
        try:
            from scapy.all import sniff, wrpcap
        except ImportError:
            print("Błąd: Nie znaleziono biblioteki scapy. Zainstaluj pakiet scapy, aby użyć funkcji przechwytywania pakietów.")
            return
        # Prepare filter if target IP given
        if self.target:
            pcap_filter = f"host {self.target}"
            print(f"Rozpoczynanie przechwytywania pakietów do/z hosta {self.target} (do {self.packet_count} pakietów lub {self.timeout} sekund)...")
        else:
            pcap_filter = None
            print(f"Rozpoczynanie przechwytywania wszystkich pakietów (do {self.packet_count} pakietów lub {self.timeout} sekund)...")

        try:
            packets = sniff(count=self.packet_count, timeout=self.timeout, filter=pcap_filter)
        except PermissionError:
            print("Brak uprawnień do sniffowania. Uruchom jako administrator/root.")
            return
        except Exception as e:
            print(f"Błąd sniffowania: {e}")
            return

        wrpcap("capture.pcap", packets)
        print(f"Zapisano przechwycone pakiety do pliku capture.pcap (liczba pakietów: {len(packets)}).")
        print("Użyj np. Wireshark aby przeanalizować zapisane pakiety.")
