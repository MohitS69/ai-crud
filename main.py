"""FastAPI CRUD application with clean architecture."""
from fastapi import FastAPI

from presentation.api.routes import router as products_router


app = FastAPI(
    title="Product Catalog API",
    description="A CRUD API for managing products with clean architecture",
    version="2.0.0",
)

# Register routers
app.include_router(products_router)


@app.get("/", tags=["health"])
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "Product Catalog API is running",
        "version": "2.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
