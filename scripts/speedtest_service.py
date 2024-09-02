import logging
import speedtest
from db_manager import store_results

# Configure logging
logging.basicConfig(
    filename='logs/speedtest.log',     # Log file
    level=logging.DEBUG,               # Log level
    filemode="a",
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
            logging.info(f'Storing results: Download: {download_speed} Mbps, Upload: {upload_speed} Mbps')
            store_results(download_speed, upload_speed)
        except Exception as e:
            logging.error(f'Error running speedtest: {e}')
            return None, None
