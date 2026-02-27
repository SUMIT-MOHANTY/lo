from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app(config_object=None):
    app = Flask(__name__)
    CORS(app)
    
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(Config)
    
    from app.api import health_bp, status_bp
    app.register_blueprint(health_bp, url_prefix='/api/v1')
    app.register_blueprint(status_bp, url_prefix='/api/v1')
    
    return app
