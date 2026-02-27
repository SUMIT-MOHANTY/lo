from typing import Dict, Any
from app.integrations.base import BaseAPIClient, APIError
from app.config import Config

class LinkedInClient(BaseAPIClient):
    def __init__(self):
        self.api_key = Config.LINKEDIN_API_KEY
        self.api_secret = Config.LINKEDIN_API_SECRET
        self.access_token = Config.LINKEDIN_ACCESS_TOKEN
        super().__init__()
    
    def _get_credentials(self) -> Dict[str, str]:
        return {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
            'access_token': self.access_token
        }
    
    def get_profile(self) -> Dict[str, Any]:
        if 'placeholder' in self.access_token:
            raise APIError('LinkedIn API not configured - placeholder credentials', 401)
        return {'id': 'linkedin_profile', 'name': 'Demo User', 'headline': 'Developer'}
    
    def share_post(self, content: str, url: str = None) -> Dict[str, Any]:
        if 'placeholder' in self.access_token:
            raise APIError('LinkedIn API not configured - placeholder credentials', 401)
        return {'post_id': '12345', 'content': content, 'url': url}
