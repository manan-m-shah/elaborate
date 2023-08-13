import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
