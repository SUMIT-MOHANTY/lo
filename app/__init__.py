from flask import Flask
from app.config import Config
from app.api import register_routes
from app.models.analytics import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

db_session = None

def get_db():
    global db_session
    if db_session is None:
        engine = create_engine(Config.DATABASE_URL or 'sqlite:///portfolio.db')
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine)
        db_session = scoped_session(session_factory)
    return db_session

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    register_routes(app)
    
    # Register analytics middleware
    from app.middleware.analytics import track_visitor
    @app.before_request
    def before_request():
        track_visitor()
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        if db_session:
            db_session.remove()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
