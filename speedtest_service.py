import speedtest

class SpeedTestService:
    def __init__(self):
        self.st = speedtest.Speedtest()

    def run_speedtest(self):
        download_speed = self.st.download() / 1_000_000  # Convert to Mbps
        upload_speed = self.st.upload() / 1_000_000  # Convert to Mbps
        return download_speed, upload_speed
