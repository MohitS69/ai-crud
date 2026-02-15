"""In-memory implementation of ProductRepository with mock data."""
from typing import Dict, List, Optional
from uuid import UUID, uuid4

from domain.entities import Product
from application.interfaces import ProductRepository


class InMemoryProductRepository(ProductRepository):
    """In-memory repository implementation using a dictionary."""
    
    def __init__(self):
        """Initialize the in-memory storage with mock data."""
        self._storage: Dict[UUID, Product] = {}
        self._initialize_mock_data()
    
    def _initialize_mock_data(self):
        """Initialize repository with 10 mock products."""
        mock_products = [
            Product(
                id=uuid4(),
                name="Wireless Mouse",
                description="Ergonomic wireless mouse with precision tracking",
                price=29.99,
                category="Electronics"
            ),
            Product(
                id=uuid4(),
                name="Mechanical Keyboard",
                description="RGB backlit mechanical keyboard with blue switches",
                price=89.99,
                category="Electronics"
            ),
            Product(
                id=uuid4(),
                name="USB-C Hub",
                description="7-in-1 USB-C hub with HDMI and ethernet",
                price=45.99,
                category="Electronics"
            ),
            Product(
                id=uuid4(),
                name="Laptop Stand",
                description="Adjustable aluminum laptop stand",
                price=39.99,
                category="Accessories"
            ),
            Product(
                id=uuid4(),
                name="Webcam HD",
                description="1080p HD webcam with built-in microphone",
                price=59.99,
                category="Electronics"
            ),
            Product(
                id=uuid4(),
                name="Desk Lamp",
                description="LED desk lamp with adjustable brightness",
                price=34.99,
                category="Accessories"
            ),
            Product(
                id=uuid4(),
                name="Monitor 27\"",
                description="27-inch 4K UHD monitor with HDR support",
                price=399.99,
                category="Electronics"
            ),
            Product(
                id=uuid4(),
                name="Headphones",
                description="Noise-cancelling over-ear headphones",
                price=149.99,
                category="Electronics"
            ),
            Product(
                id=uuid4(),
                name="Phone Stand",
                description="Adjustable phone stand for desk",
                price=19.99,
                category="Accessories"
            ),
            Product(
                id=uuid4(),
                name="Cable Organizer",
                description="Cable management box for desk organization",
                price=24.99,
                category="Accessories"
            ),
        ]
        
        for product in mock_products:
            self._storage[product.id] = product
    
    def create(self, product: Product) -> Product:
        """Create a new product in storage."""
        self._storage[product.id] = product
        return product
    
    def get_by_id(self, product_id: UUID) -> Optional[Product]:
        """Get product by ID from storage."""
        return self._storage.get(product_id)
    
    def get_all(self) -> List[Product]:
        """Get all products from storage."""
        return list(self._storage.values())
    
    def update(self, product_id: UUID, product: Product) -> Optional[Product]:
        """Update an existing product in storage."""
        if product_id not in self._storage:
            return None
        self._storage[product_id] = product
        return product
    
    def delete(self, product_id: UUID) -> bool:
        """Delete a product from storage."""
        if product_id in self._storage:
            del self._storage[product_id]
            return True
        return False
