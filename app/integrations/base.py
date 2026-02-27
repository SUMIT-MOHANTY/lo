from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import os

class APIError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class BaseAPIClient(ABC):
    def __init__(self):
        self.credentials = self._get_credentials()
    
    @abstractmethod
    def _get_credentials(self) -> Dict[str, str]:
        pass
    
    @abstractmethod
    def get_profile(self) -> Dict[str, Any]:
        pass
    
    def _make_request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        headers = kwargs.get('headers', {})
        headers['Authorization'] = f"Bearer {self.credentials.get('access_token', '')}"
        kwargs['headers'] = headers
        return {'status': 'success', 'data': {}}
