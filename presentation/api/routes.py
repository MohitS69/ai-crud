"""FastAPI routes for CRUD operations."""
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from application.services import ProductService
from presentation.api.dependencies import get_product_service
from presentation.api.schemas import ProductCreate, ProductUpdate, ProductResponse


router = APIRouter(prefix="/products", tags=["products"])
templates = Jinja2Templates(directory="presentation/templates")


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def products_page(
    request: Request,
    service: ProductService = Depends(get_product_service),
):
    """Render HTML page with all products."""
    products = service.get_all_products()
    return templates.TemplateResponse(
        "products.html",
        {"request": request, "products": products}
    )


@router.post(
    "/api",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new product",
    description="Create a new product with the provided details.",
)
def create_product(
    product_data: ProductCreate,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse:
    """Create a new product."""
    try:
        product = service.create_product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            category=product_data.category,
        )
        return ProductResponse.model_validate(product)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/api",
    response_model=List[ProductResponse],
    summary="Get all products",
    description="Retrieve a list of all products.",
)
def get_all_products(
    service: ProductService = Depends(get_product_service),
) -> List[ProductResponse]:
    """Get all products."""
    products = service.get_all_products()
    return [ProductResponse.model_validate(product) for product in products]


@router.get(
    "/api/{product_id}",
    response_model=ProductResponse,
    summary="Get product by ID",
    description="Retrieve a specific product by its unique identifier.",
)
def get_product(
    product_id: UUID,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse:
    """Get product by ID."""
    product = service.get_product(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found",
        )
    return ProductResponse.model_validate(product)


@router.put(
    "/api/{product_id}",
    response_model=ProductResponse,
    summary="Update a product",
    description="Update an existing product with the provided details.",
)
def update_product(
    product_id: UUID,
    product_data: ProductUpdate,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse:
    """Update an existing product."""
    try:
        product = service.update_product(
            product_id=product_id,
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            category=product_data.category,
        )
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found",
            )
        return ProductResponse.model_validate(product)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    "/api/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a product",
    description="Delete a product by its unique identifier.",
)
def delete_product(
    product_id: UUID,
    service: ProductService = Depends(get_product_service),
) -> None:
    """Delete a product."""
    deleted = service.delete_product(product_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found",
        )
