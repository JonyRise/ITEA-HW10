class User:
    role:str
    def __init__(self, login, password):
        self.login = login
        self.__password = password
    
    def get_password(self):
        return self.__password
    
    def get_uniq_key(self):
        return f"{self.login}_{self.role}"

class Subscriber(User):
    role = 'subscriber'

class Admin(User):
    role = 'admin'

class Author(User):
    role = 'author'
