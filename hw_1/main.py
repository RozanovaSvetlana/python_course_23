from fastapi import FastAPI

from hw_1.router import routers

app = FastAPI()

app.include_router(routers)
