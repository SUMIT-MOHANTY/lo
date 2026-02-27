from app.models import SessionLocal
from app.models.user import User

class UserService:
    def __init__(self):
        self.session = SessionLocal()
    
    def get_all_users(self):
        return self.session.query(User).all()
    
    def get_user_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id).first()
    
    def create_user(self, username, email):
        user = User(username=username, email=email)
        self.session.add(user)
        self.session.commit()
        return user
    
    def close(self):
        self.session.close()
