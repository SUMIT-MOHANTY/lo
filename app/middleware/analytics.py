from flask import request, g
from app.services.analytics_service import AnalyticsService
from app import get_db

EXCLUDED_PATHS = ['/admin', '/api', '/static']

def track_visitor():
    if request.method != 'GET':
        return
    
    path = request.path
    if any(path.startswith(excluded) for excluded in EXCLUDED_PATHS):
        return
    
    try:
        db = next(get_db())
        service = AnalyticsService(db)
        service.track_page_view(
            path=path,
            user_agent=request.headers.get('User-Agent'),
            ip=request.remote_addr,
            referrer=request.referrer
        )
    except Exception as e:
        # Don't break the app if tracking fails
        pass
