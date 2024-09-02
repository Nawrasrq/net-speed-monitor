import logging
import speedtest

# Configure logging
logging.basicConfig(
    filename='speedtest_service.log',  # Log file
    level=logging.DEBUG,              # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SpeedTestService:
    def __init__(self):
        logging.info('Initializing SpeedTestService')
        self.st = speedtest.Speedtest()

    def run_speedtest(self):
        try:
            logging.info('Running speedtest')
            download_speed = round(self.st.download() / 1_000_000, 2)  # Convert to Mbps
            upload_speed = round(self.st.upload() / 1_000_000, 2)  # Convert to Mbps
            logging.info(f'Download speed: {download_speed} Mbps')
            logging.info(f'Upload speed: {upload_speed} Mbps')
            return download_speed, upload_speed
        except Exception as e:
            logging.error(f'Error running speedtest: {e}')
            return None, None
