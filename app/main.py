from fastapi import (
  FastAPI
)
from fastapi.middleware.wsgi import WSGIMiddleware

from api.api_v1.api import api_router

from api.api_v2.app import flask_app


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(api_router, prefix="/api")
app.mount("/v2", WSGIMiddleware(flask_app))
# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源的请求
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头部
)