from fastapi import FastAPI

from app.router import routers

app = FastAPI()

app.include_router(routers)
