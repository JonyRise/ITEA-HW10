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


