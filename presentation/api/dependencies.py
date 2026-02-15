"""FastAPI dependency injection providers."""
from functools import lru_cache

from application.interfaces import ProductRepository
from application.services import ProductService
from infrastructure.repositories import InMemoryProductRepository


@lru_cache()
def get_repository() -> ProductRepository:
    """Get singleton instance of ProductRepository."""
    return InMemoryProductRepository()


def get_product_service() -> ProductService:
    """Get ProductService instance with injected repository.
    
    This function is designed to work with FastAPI's dependency injection.
    It creates a new service instance with the singleton repository.
    """
    return ProductService(repository=get_repository())
