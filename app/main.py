from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

# Include the API router
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Scraping API"}
