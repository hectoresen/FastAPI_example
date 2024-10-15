import os
from fastapi import FastAPI
from dotenv import load_dotenv
from controllers.item import router as item_router
from controllers.health import router as health_router
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/config")
def get_config():
    secret_id = os.getenv("SECRET_ID")
    secret_key = os.getenv("SECRET_KEY")
    return {
        "secret_key": secret_key,
        "secret_id": secret_id
    }

app.include_router(item_router)
app.include_router(health_router)
