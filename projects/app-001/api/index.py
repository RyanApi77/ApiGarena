from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "🚀 Project app-001",
        "status": "online",
        "deployed_at": "2026-09-08 20:27:10",
        "project_id": "app-001"
    }

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/info")
async def info():
    return {
        "project": "app-001",
        "deployed": "2026-09-08 20:27:10"
    }
