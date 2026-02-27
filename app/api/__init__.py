from flask import Blueprint
from app.api.health import Health_bp
from app.api.status import Status_bp
from app.api.social import Social_bp

Api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

def register_blueprints(app):
    app.register_blueprint(Health_bp)
    app.register_blueprint(Status_bp)
    app.register_blueprint(Social_bp)
