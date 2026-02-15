"""Repository interface for Product entity."""
from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from domain.entities import Product


class ProductRepository(ABC):
    """Abstract repository interface for Product entity."""
    
    @abstractmethod
    def create(self, product: Product) -> Product:
        """Create a new product."""
        pass
    
    @abstractmethod
    def get_by_id(self, product_id: UUID) -> Optional[Product]:
        """Get product by ID."""
        pass
    
    @abstractmethod
    def get_all(self) -> List[Product]:
        """Get all products."""
        pass
    
    @abstractmethod
    def update(self, product_id: UUID, product: Product) -> Optional[Product]:
        """Update an existing product."""
        pass
    
    @abstractmethod
    def delete(self, product_id: UUID) -> bool:
        """Delete a product by ID. Returns True if deleted, False if not found."""
        pass
