# № 1
'''
Розробити імітовану базу даних на основі списку
із функціоналом збереження до файлу
'''
import pickle
import json
from os import path

class BaseWorker:
    def __init__(self,file_name:str):
            self.file_name = file_name
            if not path.exists(self.file_name):
                self.write({})
    def write(data):
        pass
     
class BinaryFileWorker(BaseWorker):
    def write(self, data):
        with open(self.file_name, 'wb') as file:
            file.write(pickle.dumps(data))

    def read(self):

        with open(self.file_name, 'rb') as file:
            return pickle.loads(file.read())

class JsonFileWorker(BaseWorker):
    def write(self, data):
        with open(self.file_name, 'w') as file:
            file.write(json.dumps(data))

    def read(self):

        with open(self.file_name, 'r') as file:
            return json.loads(file.read())


class DB:
    worker_mapper = {'pckl': BinaryFileWorker,
                     'json': JsonFileWorker}
    
    def __init__(self, filename = 'db.txt'):
        self.filename = filename
        self.worker = self.__chose_worker()(self.filename)
        self.file_data = self.worker.read()

    def __chose_worker(self):
        file_ext = self.filename.split(".").pop()
        return self.worker_mapper.get(file_ext)
        
    def append(self, key, value):
        self.file_data.update({key:value})
        self.worker.write(self.file_data)

    def delete(self, key):
        del self.file_data[key]
        self.worker.write(self.file_data)

    def get(self, key):
        return self.file_data.get(key)
    
    def get_all(self):
        return self.file_data

    def flush(self):
        self.file_data.clear()
        self.worker.write(self.file_data)

    def __str__(self):
        return str(self.file_data)
    
    def __getitem__(self, number):
        return self.file_data.get(number)
# № 2
'''
Створити систему входу і регістрації із Адміністратором Автором і підписником
Зберігання в середині одного списку бази даних 
'''

class User:
    role:str
    db = DB('users.json') # singletone
    def __init__(self, login, password):
        self.login = login
        self.__password = password
    
    def register(self):
        if self.db.get(self.__get_uniq_key()):
            print(f"User with login {self.login} and role {self.role} already exists!")
            return
        self.db.append(self.__get_uniq_key(),{'login': self.login, 'password': self.__password, 'role': self.role})
        print(f"User {self.login} with role {self.role} has been registered!")

    def auth(self):
        user = self.db.get(self.__get_uniq_key())
        if user and user.get('password') == self.__password:
            print(f"User {self.login} with role {self.role} in system!")
            return True
        print("Invalid login or password!")
        return False
    
    def __get_uniq_key(self):
        return f"{self.login}_{self.role}"

class Subscriber(User):
    role = 'subscriber'

class Admin(User):
    role = 'admin'

class Author(User):
    role = 'author'

class System:
    def __init__(self, user):
        self.user:User = user

    def register(user:User):
        

    
u1 = Subscriber('jony_rise', 123)
u2 = Admin('jony_rise_adm', 456)
u1.register()

