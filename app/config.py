from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MAX_PAGES: int = 5
    STATIC_TOKEN: str = "my_static_token"
    PROXY: str = "None"
    SCRAPING_URL: str = "https://dentalstall.com/shop"

    class Config:
        env_file = ".env"

settings = Settings()
