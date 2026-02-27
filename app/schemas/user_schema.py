class UserSchema:
    @staticmethod
    def validate_user(data):
        errors = []
        if 'username' not in data or len(data['username']) < 3:
            errors.append('username must be at least 3 characters')
        if 'email' not in data or '@' not in data['email']:
            errors.append('invalid email format')
        return errors
