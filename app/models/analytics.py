from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PageView(Base):
    __tablename__ = 'page_views'
    
    id = Column(Integer, primary_key=True)
    path = Column(String(500), nullable=False)
    user_agent = Column(String(200))
    ip_hash = Column(String(8), nullable=False)
    referrer = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)

class DailyMetric(Base):
    __tablename__ = 'daily_metrics'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True, nullable=False)
    page_views = Column(Integer, default=0)
    unique_visitors = Column(Integer, default=0)
