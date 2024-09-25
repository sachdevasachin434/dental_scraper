class InMemoryCache:
    def __init__(self):
        self.cache = {}

    def is_price_changed(self, product_title: str, new_price: float) -> bool:
        old_price = self.cache.get(product_title)
        if old_price is None or old_price != new_price:
            self.cache[product_title] = new_price
            return True
        return False
