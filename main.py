from fastapi import FastAPI
from app.routes import github_routes

app = FastAPI()
app.include_router(github_routes.router)
