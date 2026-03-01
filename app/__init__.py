import os
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', '0') == '1'
    
    @app.route('/')
    def index():
        return jsonify({
            'status': 'running',
            'message': 'Deployment Preview System API',
            'version': '1.0.0'
        })
    
    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy'}), 200
    
    return app
