#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import uvicorn
import os

app = FastAPI(
    title="入廠證件辨識服務 API 文件",
    description="OCR Recognition API Documentation",
    version="1.0.3"
)

@app.middleware("http")
async def add_cache_control_headers(request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.get("/openapi.json")
async def get_openapi():
    return FileResponse("openapi.json", media_type="application/json")

if __name__ == "__main__":
    print("API Documentation server starting...")
    print("Server will be available at http://0.0.0.0:5000/")
    print("Open your browser and navigate to the webview to see the documentation")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_level="info"
    )
