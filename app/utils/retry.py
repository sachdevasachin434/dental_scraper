import time
import requests

def retry_on_failure(func):
    def wrapper(*args, retries: int = 3, delay: int = 5, **kwargs):
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except requests.RequestException:
                print(f"Retrying after {delay} seconds...")
                time.sleep(delay)
        raise Exception("Max retries reached")
    return wrapper
