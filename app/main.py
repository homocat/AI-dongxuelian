from fastapi import (
  FastAPI
)
from fastapi.middleware.wsgi import WSGIMiddleware

from api.api_v1.api import api_router

from api.api_v2.app import flask_app


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(api_router, prefix="/v1")
app.mount("/v2", WSGIMiddleware(flask_app))