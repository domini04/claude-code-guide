"""FastAPI application for Task Manager."""

from fastapi import FastAPI

from . import database
from .routes import router

# FLAW: No proper app configuration (CORS, etc.)
app = FastAPI(
    title="Task Manager API",
    description="A simple task management API",
    version="0.1.0"
)

# Initialize database on startup
# FLAW: No proper lifecycle management
database.init_db()

# Include routes
app.include_router(router)


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Task Manager API", "version": "0.1.0"}


@app.get("/health")
def health_check():
    """Health check endpoint."""
    # FLAW: No actual health checking (database connectivity, etc.)
    return {"status": "healthy"}
