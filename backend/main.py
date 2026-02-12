from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import psycopg2

from models import Datacenter
from database import get_datacenters

app = FastAPI(
    title="Azure Datacenters API",
    description="API for retrieving Azure datacenter locations",
    version="1.0.0"
)

# Configure CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Root endpoint providing API information."""
    return {
        "name": "Azure Datacenters API",
        "version": "1.0.0",
        "endpoints": {
            "datacenters": "/datacenters"
        }
    }


@app.get("/datacenters", response_model=List[Datacenter])
def get_datacenters_endpoint():
    """
    Get all datacenters.

    Returns a JSON list of datacenters with id, name, country, and city.
    """
    try:
        datacenters = get_datacenters()
        return datacenters
    except psycopg2.OperationalError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database connection error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
