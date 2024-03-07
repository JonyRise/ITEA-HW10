from db.storage import DB
from users import User
# № 1
'''
Розробити імітовану базу даних на основі списку
із функціоналом збереження до файлу
'''
# № 2
'''
Створити систему входу і регістрації із Адміністратором Автором і підписником
Зберігання в середині одного списку бази даних 
'''


class UserAuthenticate:
    user_db = DB('users.json') # singletone
    system_user:User

    def register(self, user:User):
        if self.user_db.get(user.get_uniq_key()):
            print(f"User with login {user.login} and role {user.role} already exists!")
            return
        self.user_db.append(user.get_uniq_key(), {'login': user.login, 'password': user.get_password(), 'role': user.role})
        print(f"User {user.login} with role {user.role} has been registered!")
        
    def auth(self, user:User):
        user_in_db = self.user_db.get(user.get_uniq_key())
        if user_in_db and user_in_db.get('password') == user.get_password():
            print(f"User {user.login} with role {user.role} in system!")
            self.system_user = user
            return True
        print("Invalid login or password!")
        return False

