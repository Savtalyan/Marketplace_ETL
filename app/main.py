from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging 
import time 

from app.core.config import settings
from app.core.database import create_db_and_tables
from app.utils.logger import setup_logging

# setup logging first
setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup : initializing resources
    logging.info("Application starting up...")

    create_db_and_tables()
    # TODO init HTTP client session

    yield # run app 


    # Shutdown : Cleanup
    logging.info("Application shutting down...")

    # TODO close database connection
    # TODO close HTTP connection
    
# create FastAPI app instance
app = FastAPI(
    title="Marketplace ETL API",
    description="An applicaiton for scraping and loading marketplace data",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request timing middleware 
@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logging.info(f"Request {request.method} {request.url} completed in {process_time:.4f}s")
    return response


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logging.error(f"Unhandled exception : {exc}", exc_info=True)
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content = {"detail": "Internal server error"}
    )


# Health check endpoint 
@app.get("/", tags=["root"])
async def root():
    """Root endpoint with API information"""
    return {
        "message" : f"{app.title}",
        "version" : f"{app.version}",
        "docs" : f"{app.docs_url}",
        "health" : "/health"
    }

# TODO import and include routers will be added here later 

# from app.api.routes import etl, marketplace, storage, monitoring
# app.include_router(etl.router, prefix="/api/v1", tags=["etl"])
# app.include_router(marketplaces.router, prefix="/api/v1", tags=["marketplaces"])
# app.include_router(storage.router, prefix="/api/v1"), tags=["storage"]
# app.include_router(monitoring.router, prefix="/api/v1", tags=["monitoring"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
