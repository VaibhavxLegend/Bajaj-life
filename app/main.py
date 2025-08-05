import uvicorn
from fastapi import FastAPI
from app.config import settings
from app.api.routes import router as hackrx_router


# Create FastAPI application instance
app = FastAPI(
    title="LLM-Powered Query–Retrieval API",
    version="1.0.0",
    description="Process documents, perform semantic search, and return structured JSON responses"
)

# Include the hackrx endpoint router under /api/v1
app.include_router(
    hackrx_router,
    prefix="/api/v1",
    tags=["hackrx"]
)


@app.on_event("startup")
async def startup_event():
    """
    Called when the application starts up.
    Could be used to initialize connections (e.g., Pinecone, database).
    """
    # Example: Initialize Pinecone index
    # await init_pinecone(settings.PINECONE_API_KEY, settings.PINECONE_ENV)
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """
    Called when the application is shutting down.
    Clean up resources (e.g., close database sessions).
    """
    # Example: Close database connection
    # await db_session.close()
    pass


if __name__ == "__main__":
    # Entry point for local development
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
