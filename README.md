# FastAPI Learning App

This is a FastAPI application created for learning purposes. Each endpoint demonstrates a specific feature or concept of FastAPI, showcasing its capabilities in building modern web APIs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rushabh7399/fastapi-app.git
   cd fastapi-app
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### 1. GET /
- **Description**: Basic endpoint that returns a simple greeting.
- **Feature Demonstrated**: Basic routing and response.
- **Response**: `"Hello"`

### 2. POST /users
- **Description**: Creates a new user with validation.
- **Feature Demonstrated**: Request body validation using Pydantic models, response models.
- **Request Body**:
  ```json
  {
    "name": "string",
    "surname": "string",
    "age": 0,
    "password": "string",
    "email": "email@example.com"
  }
  ```
- **Response Model**: Excludes password from response.
  ```json
  {
    "name": "string",
    "surname": "string",
    "age": 0
  }
  ```

### 3. GET /post_get/
- **Description**: Returns a collection of posts.
- **Feature Demonstrated**: Returning complex data structures with Pydantic models.
- **Response**: Dictionary with post objects.

### 4. GET /posts/{post_id}
- **Description**: Retrieves a post by ID with a query parameter.
- **Feature Demonstrated**: Path parameters and query parameters.
- **Parameters**:
  - `post_id` (path): string
  - `query` (query): string
- **Response**: `{"Post ID": "query_value"}`

### 5. POST /posts
- **Description**: Creates a new post.
- **Feature Demonstrated**: POST requests with request bodies.
- **Request Body**:
  ```json
  {
    "post_id": "string",
    "details": "string"
  }
  ```
- **Response**: `{"Post": {...}}`

### 6. GET /tests/{post_id}
- **Description**: Similar to endpoint 4, but with query validation.
- **Feature Demonstrated**: Query parameter validation (minimum length).
- **Parameters**:
  - `post_id` (path): string
  - `query` (query): string (min length 6), optional

### 7. GET /query/{query_id}
- **Description**: Demonstrates complex query parameters with nested models.
- **Feature Demonstrated**: Complex query parameters using Pydantic models with `extra="allow"`.
- **Parameters**:
  - `query_id` (path): string
  - `query` (query): DataQuery object with nested fields

### 8. GET /query1/{query_id}
- **Description**: Same as endpoint 7, another example.
- **Feature Demonstrated**: Reusing complex query models.

### 9. PUT /items/{item_id}
- **Description**: Updates an item with datetime and time handling.
- **Feature Demonstrated**: Handling datetime, time, and timedelta in request bodies, complex calculations.
- **Parameters**:
  - `item_id` (path): UUID
  - Request body with `start_datetime`, `end_datetime`, `process_after`, `repeat_at`
- **Response**: Calculated values including duration.

### 10. GET /shreya/{user_id}
- **Description**: Conditional response based on user_id.
- **Feature Demonstrated**: Custom responses (RedirectResponse, JSONResponse).
- **Parameters**:
  - `user_id` (path): string
- **Response**: Redirects to cricbuzz.com if user_id is "eat", otherwise JSON response.

### 11. GET /teleport
- **Description**: Returns a JSON message.
- **Feature Demonstrated**: JSONResponse usage.

### 12. GET /items_details/{item_id}
- **Description**: Retrieves item details with response model filtering.
- **Feature Demonstrated**: `response_model_exclude_unset` to exclude unset fields.
- **Parameters**:
  - `item_id` (path): string
- **Response**: Item object with unset fields excluded.

### 13. GET /items/{item_id}/name
- **Description**: Retrieves item name and description.
- **Feature Demonstrated**: `response_model_include` to include only specific fields.
- **Parameters**:
  - `item_id` (path): string
- **Response**: Item with only name and description.

### 14. GET /items/{item_id}/public
- **Description**: Retrieves public item data.
- **Feature Demonstrated**: `response_model_exclude` to exclude sensitive fields like tax.
- **Parameters**:
  - `item_id` (path): string
- **Response**: Item without tax field.

## Features Demonstrated

This app covers various FastAPI features:
- Basic routing (GET, POST, PUT)
- Path and query parameters
- Request and response validation with Pydantic
- Custom response types (JSON, Redirect)
- Datetime and time handling
- Response model filtering (include/exclude)
- UUID parameters
- Complex nested models
- Conditional responses

Use the `/docs` endpoint to explore the API interactively with Swagger UI.