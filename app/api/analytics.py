from flask import Blueprint, request, jsonify, render_template, session
from app import get_db
from app.services.analytics_service import AnalyticsService

analytics_bp = Blueprint('analytics', __name__, url_prefix='/api/analytics')

@analytics_bp.route('/track', methods=['POST'])
def track_page_view():
    data = request.get_json() or {}
    path = data.get('path', '/')
    user_agent = request.headers.get('User-Agent')
    referrer = data.get('referrer')
    ip = request.remote_addr
    
    db = next(get_db())
    service = AnalyticsService(db)
    service.track_page_view(path=path, user_agent=user_agent, ip=ip, referrer=referrer)
    
    return jsonify({'status': 'tracked'}), 201

@analytics_bp.route('/summary', methods=['GET'])
def get_summary():
    db = next(get_db())
    service = AnalyticsService(db)
    summary = service.get_summary()
    return jsonify(summary), 200

@analytics_bp.route('/daily', methods=['GET'])
def get_daily_metrics():
    days = request.args.get('days', 30, type=int)
    db = next(get_db())
    service = AnalyticsService(db)
    metrics = service.get_daily_metrics(days=days)
    
    return jsonify([{
        'date': m.date.isoformat(),
        'page_views': m.page_views,
        'unique_visitors': m.unique_visitors
    } for m in metrics]), 200

@analytics_bp.route('/pages', methods=['GET'])
def get_top_pages():
    db = next(get_db())
    service = AnalyticsService(db)
    summary = service.get_summary()
    return jsonify(summary['top_pages']), 200

# Admin dashboard route
admin_analytics_bp = Blueprint('admin_analytics', __name__, url_prefix='/admin')

@admin_analytics_bp.route('/analytics', methods=['GET'])
def analytics_dashboard():
    # Check admin authentication (assuming User model has is_admin field)
    # from app.models.user import User
    # user_id = session.get('user_id')
    # user = db.query(User).filter_by(id=user_id).first()
    # if not user or not getattr(user, 'is_admin', False):
    #     return jsonify({'error': 'Unauthorized'}), 401
    
    db = next(get_db())
    service = AnalyticsService(db)
    summary = service.get_summary()
    daily_metrics = service.get_daily_metrics(30)
    
    return render_template('admin/analytics.html', 
                         summary=summary,
                         daily_metrics=daily_metrics)
