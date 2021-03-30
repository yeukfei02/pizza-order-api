from fastapi import FastAPI
import os
from src.routes.main import router as main_router
from src.routes.pizza import router as pizza_router

from dotenv import load_dotenv
load_dotenv()

fastapi_env = os.getenv('FASTAPI_ENV')

app = FastAPI()

app.include_router(main_router)
app.include_router(pizza_router)
