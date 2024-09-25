from fastapi import APIRouter, Depends
from app.services.scraper import Scraper
from app.services.storage import LocalStorage
from app.services.notifier import Notifier
from app.services.cache import InMemoryCache
from app.security.auth import authenticate

router = APIRouter()

@router.post("/scrape")
async def scrape_data(max_pages: int = 5, proxy: str = None, auth_token: str = Depends(authenticate)):
    scraper = Scraper(max_pages=max_pages, proxy=proxy)
    scraped_data = scraper.scrape()

    cache = InMemoryCache()
    storage = LocalStorage()

    final_data = [product for product in scraped_data if cache.is_price_changed(product['title'], product['price'])]
    storage.save(final_data)

    notifier = Notifier()
    notifier.notify(f"Scraped {len(final_data)} products")

    return {"message": f"Scraped {len(final_data)} products"}
