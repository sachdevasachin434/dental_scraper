from fastapi import Header, HTTPException
from app.config import settings

def authenticate(auth_token: str = Header(None)):
    if auth_token != settings.STATIC_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
