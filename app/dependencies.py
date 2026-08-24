from fastapi import Header, HTTPException, status

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def verify_api_key(
        x_api_key: str | None =Header(default=None),
    )-> None:

    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API key",
        )
    
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    