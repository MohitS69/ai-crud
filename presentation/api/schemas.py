"""Pydantic schemas for request/response validation."""
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class ProductCreate(BaseModel):
    """Schema for creating a new product."""
    
    name: str = Field(..., min_length=1, max_length=100, description="Product name")
    description: str = Field(..., min_length=1, max_length=500, description="Product description")
    price: float = Field(..., gt=0, description="Product price (must be positive)")
    category: str = Field(..., min_length=1, max_length=50, description="Product category")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Laptop",
                "description": "High-performance laptop for developers",
                "price": 1299.99,
                "category": "Electronics",
            }
        }
    )


class ProductUpdate(BaseModel):
    """Schema for updating an existing product."""
    
    name: str | None = Field(None, min_length=1, max_length=100, description="Product name")
    description: str | None = Field(None, min_length=1, max_length=500, description="Product description")
    price: float | None = Field(None, gt=0, description="Product price (must be positive)")
    category: str | None = Field(None, min_length=1, max_length=50, description="Product category")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Updated Laptop",
                "price": 1199.99,
                "category": "Electronics",
            }
        }
    )


class ProductResponse(BaseModel):
    """Schema for product response."""
    
    id: UUID = Field(..., description="Product unique identifier")
    name: str = Field(..., description="Product name")
    description: str = Field(..., description="Product description")
    price: float = Field(..., description="Product price")
    category: str = Field(..., description="Product category")
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Laptop",
                "description": "High-performance laptop for developers",
                "price": 1299.99,
                "category": "Electronics",
            }
        }
    )
