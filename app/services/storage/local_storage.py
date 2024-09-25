import json
from app.services.storage.storage import StorageInterface


class LocalStorage(StorageInterface):
    def __init__(self, file_path='local_storage.json'):
        self.file_path = file_path
    
    def save(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)