import os
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Social Media API Credentials (placeholders)
    LINKEDIN_API_KEY = os.getenv('LINKEDIN_API_KEY', 'placeholder_linkedin_key')
    LINKEDIN_API_SECRET = os.getenv('LINKEDIN_API_SECRET', 'placeholder_linkedin_secret')
    LINKEDIN_ACCESS_TOKEN = os.getenv('LINKEDIN_ACCESS_TOKEN', 'placeholder_linkedin_token')
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', 'placeholder_github_token')
    GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'placeholder_username')
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY', 'placeholder_twitter_key')
    TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET', 'placeholder_twitter_secret')
    TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', 'placeholder_twitter_token')
    TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET', 'placeholder_twitter_secret')
    SOCIAL_SHARE_BASE_URL = os.getenv('SOCIAL_SHARE_BASE_URL', 'https://yourdomain.com')
