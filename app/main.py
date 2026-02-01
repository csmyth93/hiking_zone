from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.routers import api

# Get the app directory
APP_DIR = Path(__file__).parent

app = FastAPI(
    title="UK Hiking Map",
    description="Interactive map showing hiking locations near London with rain forecasts"
)

# Mount static files
app.mount("/static", StaticFiles(directory=APP_DIR / "static"), name="static")

# Setup templates
templates = Jinja2Templates(directory=APP_DIR / "templates")

# Include API router
app.include_router(api.router)


@app.get("/")
async def index(request: Request):
    """Serve the main map page."""
    return templates.TemplateResponse("index.html", {"request": request})
