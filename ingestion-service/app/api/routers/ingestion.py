from fastapi import APIRouter
from app.engine.generate import generate_datasource

ingestion_router = r = APIRouter()

@r.post("")
def ingestion():
    generate_datasource()
