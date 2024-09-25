from app.services.storage.local_storage import LocalStorage
import os


class StorageFactory:
    @staticmethod
    def get_storage():
        env = os.getenv('ENVIRONMENT', 'local').lower()
        
        if env == 'prod':
            # return MySQLStorage()
            pass
        elif env == 'qa':
            # return SQLiteStorage()
            pass
        else:
            return LocalStorage()