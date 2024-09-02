import logging
from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Configure logging
logging.basicConfig(
    filename='logs/speedtest.log',     # Log file
    level=logging.DEBUG,               # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

Base = declarative_base()

class SpeedTestRecord(Base):
    __tablename__ = 'speedtest'
    id = Column(Integer, primary_key=True, autoincrement=True)
    download_speed = Column(Float, nullable=False)
    upload_speed = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now())

engine = create_engine('sqlite:///speedtest.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def store_results(download_speed, upload_speed, timestamp=datetime.datetime.now()):
    session = Session()
    record = SpeedTestRecord(download_speed=download_speed, upload_speed=upload_speed, timestamp=timestamp)
    try:
        logging.info('Storing result in database')
        session.add(record)
        session.commit()
    except Exception as e:
        logging.error(f'Error storing result: {e}')
    finally:
        session.close()
