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

user_db = DB('users.json') # singletone

def register(user:User): 
    if not user_db.get(user.get_uniq_key()):
        user_db.append(user.get_uniq_key(), {'login': user.login, 'password': user.get_password(), 'role': user.role})
        print(f"User {user.login} with role {user.role} has been registered!")
    else:
        print(f"User with login {user.login} and role {user.role} already exists!")
        
def auth(user:User):
    user_in_db = user_db.get(user.get_uniq_key())
    if user_in_db and user_in_db.get('password') == user.get_password():
        print(f"User {user.login} with role {user.role} in system!")
        return True
    print("Invalid login or password!")
    return False

