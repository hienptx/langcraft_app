# fastapi app packages
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.endpoints import api_router

from dotenv import load_dotenv
import os

app = FastAPI()
app.include_router(api_router)
# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

load_dotenv()
