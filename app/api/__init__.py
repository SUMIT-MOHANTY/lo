from flask import Blueprint

def create_api_blueprints():
    from app.api.health import health_bp
    return [health_bp]

def register_routes(app):
    for bp in create_api_blueprints():
        app.register_blueprint(bp)
