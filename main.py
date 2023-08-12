from fastapi import FastAPI
from app.routes import github_routes

# Create FastAPI instance
app = FastAPI()
app.include_router(github_routes.router)
