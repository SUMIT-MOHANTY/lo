from flask import Blueprint, jsonify, request, current_app, url_for
from app.models import db, SocialLink
from app.integrations import LinkedInClient, GitHubClient, TwitterClient, APIError

Social_bp = Blueprint('social', __name__, url_prefix='/api/social')

@Social_bp.route('/links', methods=['GET'])
def get_social_links():
    links = SocialLink.query.filter_by(is_active=True).order_by(SocialLink.sort_order).all()
    return jsonify({
        'links': [{
            'id': l.id,
            'platform': l.platform,
            'url': l.url,
            'display_name': l.display_name,
            'icon': l.icon
        } for l in links]
    })

@Social_bp.route('/links', methods=['POST'])
def create_social_link():
    data = request.get_json()
    link = SocialLink(
        platform=data.get('platform'),
        url=data.get('url'),
        display_name=data.get('display_name'),
        icon=data.get('icon'),
        is_active=data.get('is_active', True),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(link)
    db.session.commit()
    return jsonify({'id': link.id, 'platform': link.platform}), 201

@Social_bp.route('/share/options', methods=['GET'])
def get_share_options():
    url = request.args.get('url', '')
    title = request.args.get('title', '')
    base_url = current_app.config.get('SOCIAL_SHARE_BASE_URL', 'https://yourdomain.com')
    share_url = url if url else base_url
    return jsonify({
        'share_url': share_url,
        'title': title,
        'platforms': [
            {'name': 'linkedin', 'url': f'https://www.linkedin.com/shareArticle?mini=true&url={share_url}'},
            {'name': 'twitter', 'url': f'https://twitter.com/intent/tweet?url={share_url}&text={title}'},
            {'name': 'github', 'url': f'https://github.com/share?url={share_url}'}
        ]
    })

@Social_bp.route('/integrations/linkedin/profile', methods=['GET'])
def get_linkedin_profile():
    try:
        client = LinkedInClient()
        profile = client.get_profile()
        return jsonify(profile)
    except APIError as e:
        return jsonify({'error': e.message}), e.status_code or 500

@Social_bp.route('/integrations/github/user', methods=['GET'])
def get_github_user():
    try:
        client = GitHubClient()
        user = client.get_user()
        return jsonify(user)
    except APIError as e:
        return jsonify({'error': e.message}), e.status_code or 500

@Social_bp.route('/integrations/github/repos', methods=['GET'])
def get_github_repos():
    try:
        client = GitHubClient()
        repos = client.get_repos()
        return jsonify({'repos': repos})
    except APIError as e:
        return jsonify({'error': e.message}), e.status_code or 500

@Social_bp.route('/integrations/twitter/timeline', methods=['GET'])
def get_twitter_timeline():
    try:
        client = TwitterClient()
        tweets = client.get_user_timeline()
        return jsonify({'tweets': tweets})
    except APIError as e:
        return jsonify({'error': e.message}), e.status_code or 500
