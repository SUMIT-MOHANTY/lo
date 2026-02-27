import hashlib
from datetime import datetime, date, timedelta
from sqlalchemy import func, distinct
from sqlalchemy.orm import Session
from app.models.analytics import PageView, DailyMetric
from app.config import Config

class AnalyticsService:
    def __init__(self, db_session: Session):
        self.db = db_session
    
    def _hash_ip(self, ip: str) -> str:
        secret = getattr(Config, 'SECRET_KEY', 'default-secret')
        hash_input = f"{ip}{secret}".encode('utf-8')
        full_hash = hashlib.sha256(hash_input).hexdigest()
        return full_hash[:8]
    
    def track_page_view(self, path: str, user_agent: str = None, ip: str = None, referrer: str = None):
        ip_hash = self._hash_ip(ip or 'unknown')
        truncated_ua = (user_agent[:200] if user_agent else None)
        
        view = PageView(
            path=path,
            user_agent=truncated_ua,
            ip_hash=ip_hash,
            referrer=referrer
        )
        self.db.add(view)
        
        today = date.today()
        metric = self.db.query(DailyMetric).filter_by(date=today).first()
        if not metric:
            metric = DailyMetric(date=today, page_views=0, unique_visitors=0)
            self.db.add(metric)
        
        metric.page_views += 1
        
        existing_visitor = self.db.query(PageView).filter(
            PageView.ip_hash == ip_hash,
            func.date(PageView.created_at) == today
        ).first()
        
        if not existing_visitor:
            metric.unique_visitors += 1
        
        self.db.commit()
        return view
    
    def get_daily_metrics(self, days: int = 30):
        start_date = date.today() - timedelta(days=days)
        return self.db.query(DailyMetric).filter(
            DailyMetric.date >= start_date
        ).order_by(DailyMetric.date.desc()).all()
    
    def get_page_views(self, path: str = None, limit: int = 100):
        query = self.db.query(PageView)
        if path:
            query = query.filter(PageView.path == path)
        return query.order_by(PageView.created_at.desc()).limit(limit).all()
    
    def get_summary(self) -> dict:
        total_views = self.db.query(PageView).count()
        unique_visitors = self.db.query(func.count(distinct(PageView.ip_hash))).scalar() or 0
        
        today = date.today()
        today_metric = self.db.query(DailyMetric).filter_by(date=today).first()
        today_views = today_metric.page_views if today_metric else 0
        
        top_pages = self.db.query(
            PageView.path,
            func.count(PageView.id).label('views')
        ).group_by(PageView.path).order_by(func.count(PageView.id).desc()).limit(10).all()
        
        return {
            'total_views': total_views,
            'unique_visitors': unique_visitors,
            'today_views': today_views,
            'top_pages': [{'path': p.path, 'views': p.views} for p in top_pages]
        }
