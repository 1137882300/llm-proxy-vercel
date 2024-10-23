#!/usr/bin/env python3
from fastapi.middleware.cors import CORSMiddleware
from public.usage import USAGE as html
from api.hello import router as hello_router
from fastapi import FastAPI
from fastapi.responses import Response
from api.servers.generic import router as generic_router
from api.servers.gemini import router as gemini_router

app = FastAPI()

app.include_router(hello_router, prefix="/hello")
app.include_router(gemini_router, prefix="/gemini")
app.include_router(generic_router, prefix="")  # put generic last

# 允许所有来源（*表示所有）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应使用具体的域名
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)


@app.get("/")
def _root():
    return Response(content=html, media_type="text/html")
