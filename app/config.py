import os
import yaml
from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).parent.parent
    CONFIG_PATH = BASE_DIR / 'config.yaml'
    
    def __init__(self):
        self._config = self._load_config()
    
    def _load_config(self):
        if self.CONFIG_PATH.exists():
            with open(self.CONFIG_PATH, 'r') as f:
                return yaml.safe_load(f)
        return {}
    
    @property
    def database_url(self):
        db = self._config.get('database', {}).get('primary', {})
        if db.get('type') == 'sqlite':
            return f"sqlite:///{db.get('path', '/workspace/data/app.db')}"
        return "postgresql://localhost/app"
    
    @property
    def azure_openai_api_key(self):
        return os.getenv('AZURE_OPENAI_API_KEY', 
                         self._config.get('azure', {}).get('openai', {}).get('api_key', ''))
    
    @property
    def azure_openai_endpoint(self):
        return os.getenv('AZURE_OPENAI_ENDPOINT',
                         self._config.get('azure', {}).get('openai', {}).get('endpoint', ''))
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = property(database_url)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
