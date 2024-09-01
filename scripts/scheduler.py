import schedule
import time
from run_speedtest import run_speedtest
from db_manager import store_results, Session

def job():
    session = Session()
    download_speed, upload_speed = run_speedtest()
    store_results(session, download_speed, upload_speed)
    session.close()

schedule.every(3).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
