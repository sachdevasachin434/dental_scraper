import json
from typing import List
from app.models.product import Product

class LocalStorage:
    def __init__(self, file_path: str = 'scraped_data.json'):
        self.file_path = file_path

    def save(self, data: List[Product]):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)
