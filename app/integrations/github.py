from typing import Dict, Any, List
from app.integrations.base import BaseAPIClient, APIError
from app.config import Config

class GitHubClient(BaseAPIClient):
    def __init__(self):
        self.token = Config.GITHUB_TOKEN
        self.username = Config.GITHUB_USERNAME
        super().__init__()
    
    def _get_credentials(self) -> Dict[str, str]:
        return {
            'token': self.token,
            'username': self.username,
            'access_token': self.token
        }
    
    def get_user(self) -> Dict[str, Any]:
        if 'placeholder' in self.token:
            raise APIError('GitHub API not configured - placeholder credentials', 401)
        return {'login': self.username, 'name': 'Demo User', 'public_repos': 0}
    
    def get_repos(self) -> List[Dict[str, Any]]:
        if 'placeholder' in self.token:
            raise APIError('GitHub API not configured - placeholder credentials', 401)
        return []
