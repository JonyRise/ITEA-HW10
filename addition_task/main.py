from users import Subscriber, Author, Admin
from authenticator import register, auth
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
register(user1)
register(user2)
print(auth(user1))
print(auth(user3))

