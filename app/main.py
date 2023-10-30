from fastapi import (
  FastAPI
)
from api.api_v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")