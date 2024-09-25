import requests
from bs4 import BeautifulSoup
from app.models.product import Product
from app.utils.retry import retry_on_failure
from app.config import settings
import pdb

class Scraper:
    def __init__(self, max_pages: int = settings.MAX_PAGES, proxy: str = settings.PROXY):
        self.max_pages = max_pages
        self.proxy = proxy
        self.session = requests.Session()
        if self.proxy:
            self.session.proxies = {'http': self.proxy, 'https': self.proxy}

    @retry_on_failure
    def scrape(self):
        scraped_data = []
        for page_num in range(1, self.max_pages + 1):
            response = self.session.get(f"{settings.SCRAPING_URL}/page/{page_num}")
            soup = BeautifulSoup(response.text, 'html.parser')

            products = soup.find('div', class_='mf-shop-content').find('ul').find_all('li')
            for product in products:
                try:
                    product_image = product.find('div', class_='mf-product-thumbnail').find('a').find('img')['data-lazy-src']
                    product_title = product.find('div', class_='mf-product-details').find('h2', class_='woo-loop-product__title').get_text(strip=True)
                    # product_title = product.find('div', class_='mf-product-price-box').find('a', class_='add_to_cart_button')['data-title']
                    price_str = product.find('div', class_='mf-product-price-box').find('span', class_='woocommerce-Price-amount').get_text(strip=True).replace('₹', '').replace(',', '').strip()
                    product_price = float(price_str)
                    scraped_data.append(Product(
                        title=product_title,
                        price=product_price,
                        image_path=product_image
                    ).dict())
                except Exception as e:
                    print(e)
        return scraped_data
