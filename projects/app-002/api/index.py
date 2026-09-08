from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "🚀 Project app-002",
        "status": "online",
        "deployed_at": "2026-09-08 20:27:10",
        "project_id": "app-002"
    }

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/info")
async def info():
    return {
        "project": "app-002",
        "deployed": "2026-09-08 20:27:10"
    }
