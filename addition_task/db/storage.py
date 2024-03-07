from .file_workers import BinaryFileWorker, JsonFileWorker

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