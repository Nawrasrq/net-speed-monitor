import logging
from speedtest_service import SpeedTestService
from db_manager import store_results

# Configure logging
logging.basicConfig(
    filename='run_speedtest.log',  # Log file
    level=logging.DEBUG,          # Log level
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info('Starting run_speedtest script')
    service = SpeedTestService()
    download_speed, upload_speed = service.run_speedtest()
    if download_speed is not None and upload_speed is not None:
        logging.info(f'Storing results: Download: {download_speed} Mbps, Upload: {upload_speed} Mbps')
        store_results(download_speed, upload_speed)
    else:
        logging.error('Failed to get speedtest results')

if __name__ == "__main__":
    main()
