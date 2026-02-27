from flask import jsonify
from datetime import datetime
from app.api import status_bp

@status_bp.route('/status', methods=['GET'])
def app_status():
    return jsonify({
        'application': 'FlaskAppSkeleton',
        'version': '1.0.0',
        'status': 'running',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }), 200
