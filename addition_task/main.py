from users import Subscriber, Author, Admin
from authenticator import UserAuthenticate
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

user1 = Subscriber('user1', 123)
user2 = Author('user2', 456)
user3 = Admin('user3', 789)
authenticator = UserAuthenticate()
authenticator.register(user1)
authenticator.register(user2)
authenticator.register(user3)
authenticator.auth(user1)
print(authenticator.system_user)
authenticator.auth(user2)
print(authenticator.system_user)
authenticator.auth(user3)
print(authenticator.system_user)

