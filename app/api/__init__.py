from flask import Blueprint
health_bp = Blueprint('health', __name__)
status_bp = Blueprint('status', __name__)

from app.api import health, status
