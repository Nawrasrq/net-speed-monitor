from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class SpeedTestRecord(Base):
    __tablename__ = 'speedtest'
    id = Column(Integer, primary_key=True, autoincrement=True)
    download_speed = Column(Float, nullable=False)
    upload_speed = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now())

engine = create_engine('sqlite:///speedtest.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def store_results(session, download_speed, upload_speed):
    result = SpeedTestRecord(download_speed=download_speed, upload_speed=upload_speed)
    session.add(result)
    session.commit()
