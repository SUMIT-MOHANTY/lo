from typing import Dict, Any, List
from app.integrations.base import BaseAPIClient, APIError
from app.config import Config

class TwitterClient(BaseAPIClient):
    def __init__(self):
        self.api_key = Config.TWITTER_API_KEY
        self.api_secret = Config.TWITTER_API_SECRET
        self.access_token = Config.TWITTER_ACCESS_TOKEN
        self.access_secret = Config.TWITTER_ACCESS_SECRET
        super().__init__()
    
    def _get_credentials(self) -> Dict[str, str]:
        return {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
            'access_token': self.access_token,
            'access_secret': self.access_secret
        }
    
    def post_tweet(self, content: str) -> Dict[str, Any]:
        if 'placeholder' in self.access_token:
            raise APIError('Twitter API not configured - placeholder credentials', 401)
        return {'id': '12345', 'text': content}
    
    def get_user_timeline(self, count: int = 10) -> List[Dict[str, Any]]:
        if 'placeholder' in self.access_token:
            raise APIError('Twitter API not configured - placeholder credentials', 401)
        return []
