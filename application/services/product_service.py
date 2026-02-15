"""Service layer for Product business logic."""
from typing import List, Optional
from uuid import UUID

from domain.entities import Product
from application.interfaces import ProductRepository


class ProductService:
    """Service class handling Product business logic."""
    
    def __init__(self, repository: ProductRepository):
        """Initialize service with repository dependency."""
        self.repository = repository
    
    def create_product(
        self,
        name: str,
        description: str,
        price: float,
        category: str,
    ) -> Product:
        """Create a new product."""
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        product = Product(
            name=name,
            description=description,
            price=price,
            category=category,
        )
        return self.repository.create(product)
    
    def get_product(self, product_id: UUID) -> Optional[Product]:
        """Get product by ID."""
        return self.repository.get_by_id(product_id)
    
    def get_all_products(self) -> List[Product]:
        """Get all products."""
        return self.repository.get_all()
    
    def update_product(
        self,
        product_id: UUID,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[float] = None,
        category: Optional[str] = None,
    ) -> Optional[Product]:
        """Update an existing product."""
        if price is not None and price < 0:
            raise ValueError("Price cannot be negative")
        
        product = self.repository.get_by_id(product_id)
        if product is None:
            return None
        
        product.update(
            name=name,
            description=description,
            price=price,
            category=category,
        )
        return self.repository.update(product_id, product)
    
    def delete_product(self, product_id: UUID) -> bool:
        """Delete a product."""
        return self.repository.delete(product_id)
