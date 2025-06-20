import airsim

class AirSimClientWrapper:
    def __init__(self, ip="127.0.0.1"):
        self.ip = ip
        self.client = airsim.MultirotorClient(ip=self.ip)

    def connect(self):
        try:
            self.client.confirmConnection()
            self.client.enableApiControl(True)
            self.client.armDisarm(True)
            return self.client
        except Exception as e:
            raise RuntimeError(f"Failed to connect to AirSim at {self.ip}: {e}")

    def disconnect(self):
        try:
            self.client.landAsync().join()
            self.client.armDisarm(False)
            self.client.enableApiControl(False)
        except:
            pass  # Fail-safe cleanup
