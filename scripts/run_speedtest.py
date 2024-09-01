from speedtest_service import SpeedTestService
from db_manager import store_results, Session

def run_speedtest():
    st = SpeedTestService()
    download_speed, upload_speed = st.run_speedtest()
    return download_speed, upload_speed

def main():
    session = Session()
    download_speed, upload_speed = run_speedtest()
    store_results(session, download_speed, upload_speed)
    session.close()

if __name__ == "__main__":
    main()
