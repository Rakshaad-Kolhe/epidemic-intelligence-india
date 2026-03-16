import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
API_VERSION = os.getenv("API_VERSION", "v1")
APP_NAME = os.getenv("APP_NAME", "Epidemic Intelligence API")
