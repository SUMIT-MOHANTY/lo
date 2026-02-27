from flask import Blueprint
from app.api.health import health_bp
from app.api.status import status_bp
from app.api.social import social_bp
from app.api.analytics import analytics_bp, admin_analytics_bp

api_bp = Blueprint('api', __name__)

def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(status_bp)
    app.register_blueprint(social_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(admin_analytics_bp)
