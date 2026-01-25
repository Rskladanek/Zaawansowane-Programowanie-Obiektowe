"""
Base class for network tools, storing target information and common interface.
"""
class NetworkTool:
    def __init__(self, target_ip):
        # Use encapsulated attribute for target IP
        self._target = target_ip

    @property
    def target(self):
        """Get or set the target IP address."""
        return self._target

    @target.setter
    def target(self, new_ip):
        # Optionally, we could validate IP format here
        self._target = new_ip

    def execute(self):
        raise NotImplementedError("Subclasses should implement this method.")
