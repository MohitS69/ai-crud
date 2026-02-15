"""Domain entity for Product."""
from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class Product:
    """Product domain entity representing a product in the catalog."""
    
    name: str
    description: str
    price: float
    category: str
    id: UUID = None
    
    def __post_init__(self):
        """Generate ID if not provided."""
        if self.id is None:
            self.id = uuid4()
    
    def update(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[float] = None,
        category: Optional[str] = None,
    ) -> None:
        """Update product attributes."""
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if category is not None:
            self.category = category
