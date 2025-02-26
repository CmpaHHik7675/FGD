from models.user import User

def create_user(username, email):
    return User(username, email)
