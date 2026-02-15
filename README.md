FastAPI CRUD Application Walkthrough
Overview
Successfully implemented a complete CRUD application using FastAPI with clean architecture principles. The application uses in-memory storage, Pydantic validation, and FastAPI's built-in dependency injection system.

Project Structure
crud-py/
├── domain/
│ └── entities/
│ └── item.py # Item domain entity
├── application/
│ ├── interfaces/
│ │ └── repository.py # ItemRepository interface
│ └── services/
│ └── item_service.py # Business logic layer
├── infrastructure/
│ └── repositories/
│ └── in_memory_repository.py # In-memory implementation
├── presentation/
│ └── api/
│ ├── schemas.py # Pydantic models
│ ├── routes.py # FastAPI routes
│ └── dependencies.py # DI providers
├── main.py # Application entry point
└── requirements.txt # Dependencies
Implementation Details
Domain Layer
item.py

Pure domain entity with no framework dependencies
Dataclass-based
Item
entity with attributes:
id
, name, description, price, is_available
Auto-generates UUID if not provided
Includes
update()
method for modifying attributes
Application Layer
repository.py

Abstract
ItemRepository
interface defining CRUD contract
Methods:
create
,
get_by_id
,
get_all
,
update
,
delete
item_service.py

Business logic layer with validation rules
Price validation (must be positive)
Depends on
ItemRepository
interface (dependency inversion)
Infrastructure Layer
in_memory_repository.py

Concrete implementation using Python dictionary
Thread-safe for single-process usage
Implements all
ItemRepository
methods
Presentation Layer
schemas.py

ItemCreate
: Request schema with validation (min/max length, positive price)
ItemUpdate
: Optional fields for partial updates
ItemResponse
: Response schema with UUID serialization
Includes OpenAPI examples for documentation
dependencies.py

get_repository()
: Singleton repository instance using @lru_cache
get_item_service()
: Service factory with injected repository
routes.py

RESTful API endpoints with proper HTTP status codes
Comprehensive error handling (404, 400)
OpenAPI documentation with descriptions
main.py

FastAPI application initialization
Router registration
Health check endpoint
API Endpoints
Method Endpoint Description Status Code
GET / Health check 200
POST /items/ Create new item 201
GET /items/ Get all items 200
GET /items/{id} Get item by ID 200/404
PUT /items/{id} Update item 200/404
DELETE /items/{id} Delete item 204/404
Verification Results
Environment Setup
bash
uv venv # Created virtual environment
uv pip install -r requirements.txt # Installed 18 packages
Server Startup
bash
uvicorn main:app --reload

# INFO: Uvicorn running on http://127.0.0.1:8000

# INFO: Application startup complete

Testing Results
✅ CREATE - POST /items/
bash
curl -X POST "http://127.0.0.1:8000/items/" \
 -H "Content-Type: application/json" \
 -d '{"name": "Laptop", "description": "High-performance laptop", "price": 1299.99}'
Response (201):

json
{
"id": "c9c08352-415d-456f-934c-3124e15a25f2",
"name": "Laptop",
"description": "High-performance laptop for developers",
"price": 1299.99,
"is_available": true
}
✅ READ ALL - GET /items/
bash
curl -X GET "http://127.0.0.1:8000/items/"
Response (200): Array of all items

✅ READ ONE - GET /items/{id}
bash
curl -X GET "http://127.0.0.1:8000/items/c9c08352-415d-456f-934c-3124e15a25f2"
Response (200): Single item object

✅ UPDATE - PUT /items/{id}
bash
curl -X PUT "http://127.0.0.1:8000/items/c9c08352-415d-456f-934c-3124e15a25f2" \
 -H "Content-Type: application/json" \
 -d '{"name": "Gaming Laptop", "price": 1499.99}'
Response (200):

json
{
"id": "c9c08352-415d-456f-934c-3124e15a25f2",
"name": "Gaming Laptop",
"description": "High-performance laptop for developers",
"price": 1499.99,
"is_available": true
}
Note: Only specified fields were updated, others remained unchanged

✅ DELETE - DELETE /items/{id}
bash
curl -X DELETE "http://127.0.0.1:8000/items/8cd277fb-45f6-43d6-88e5-77e90ddab454"
Response (204): No content

✅ Health Check - GET /
bash
curl -X GET "http://127.0.0.1:8000/"
Response (200):

json
{
"status": "healthy",
"message": "CRUD API is running"
}
Key Features
✅ Clean Architecture
Clear separation of concerns across layers
Domain entities independent of frameworks
Dependency inversion (service depends on interface, not implementation)
✅ FastAPI Dependency Injection
Singleton repository using @lru_cache
Service factory pattern with Depends()
No external DI container needed
✅ Pydantic Validation
Automatic request validation
Type safety with Python type hints
OpenAPI schema generation
✅ RESTful Design
Proper HTTP methods and status codes
JSON request/response format
Comprehensive error handling
✅ Developer Experience
Auto-reload with Uvicorn
Interactive API docs at /docs
Type hints throughout codebase
Next Steps
To extend this application, consider:

Database Integration: Replace in-memory repository with PostgreSQL/MongoDB
Authentication: Add JWT-based auth with FastAPI security utilities
Testing: Add pytest tests for all layers
Pagination: Implement pagination for GET /items/
Filtering: Add query parameters for filtering items
Docker: Containerize the application
CI/CD: Set up automated testing and deployment
Running the Application
bash

# Activate virtual environment

source .venv/bin/activate

# Start the server

uvicorn main:app --reload

# Access interactive docs

# Open browser: http://127.0.0.1:8000/docs
