from db.database import db

class User:
    def __init__(self, username:str, email:str, token:str) -> None:
        self.username = username
        self.email = email
        self.token = token
    
    @classmethod
    def user_exists(cls, username:str) -> bool:
        '''
        Checks whether the specified username exists in the database.
        '''
        user = db.fetch_one("SELECT * FROM users WHERE safe_name = %s", (username.lower(),))
        return user is not None

    @classmethod
    def email_exists(cls, email:str) -> bool:
        '''
        Checks whether the specified email exists in the database.
        '''
        user = db.fetch_one("SELECT * FROM users WHERE email = %s", (email,))
        return user is not None

    
    @classmethod
    def get(cls, username:str, email:str, token:str) -> 'User':
        return cls(
            username=username,
            email=email,
            token=token
        )