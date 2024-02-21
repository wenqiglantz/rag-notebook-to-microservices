from dotenv import load_dotenv
import logging, os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.ingestion import ingestion_router

load_dotenv()

app = FastAPI()

environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'dev' if not set


if environment == "dev":
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(ingestion_router, prefix="/api/ingestion")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
