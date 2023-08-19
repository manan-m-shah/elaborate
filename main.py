from mangum import Mangum
from fastapi import FastAPI
from app.routes import github_routes

# Creating FastAPI instance
app = FastAPI()
app.include_router(github_routes.router)

# Wrapping the FastAPI app with Mangum for Lambda compatibility
handler = Mangum(app)
