import schedule
import time
import argparse
from speedtest_service import SpeedTestService
from db_manager import Session

def job():
    session = Session()
    st = SpeedTestService()
    st.run_speedtest()
    session.close()

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run speed test in scheduled mode or just once.")
    parser.add_argument('--run-once', action='store_true', help="Run the speed test once and exit.")
    args = parser.parse_args()

    if args.run_once:
        # Run speed test once
        job()
    else:
        # Schedule the job to run every 3 hours
        schedule.every(3).hours.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
