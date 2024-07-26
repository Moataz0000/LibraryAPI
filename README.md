# API - Reference 

* Date Without REST (Function-Based View)
  - This endpoint returns a list of books without using the Django REST framework.
* URL: api-books/
* Method: GET
* Respons:

```ruby
[
    {
        "id": 1,
        "title": "djanogforall",
        "slug": "djanogforall",
        "category": "programming",
        "price": "75$",
        "author": "Moataz Fawzy",
        "stock": 100,
        "creation_date": "1/1/2024"
    },
]

```
-------------------------------------------------------------------------

# API Documentation

## API Endpoints

### 1. Date Without REST (Function-Based View)
This endpoint returns a list of books without using the Django REST framework.

**URL**: `/date_without_REST`  
**Method**: `GET`  
**Response**:
```json
[
    {
        "id": 1,
        "title": "djanogforall",
        "slug": "djanogforall",
        "category": "programming",
        "price": "75$",
        "author": "Moataz Fawzy",
        "stock": 100,
        "creation_date": "1/1/2024"
    },
    {
        "id": 2,
        "title": "restframework",
        "slug": "restframework",
        "category": "programming",
        "price": "60$",
        "author": "Moataz Fawzy",
        "stock": 70,
        "creation_date": "1/12/2024"
    }
]
```

### 2. No REST from Model (Function-Based View)
This endpoint returns a list of active books from the model without using the Django REST framework.

**URL**: `/no_rest_from_model`  
**Method**: `GET`  
**Response**:
```json
{
    "queryset": [
        // List of active books
    ]
}
```

### 3. List and Create Books (Function-Based View)
This endpoint lists all active books and allows the creation of a new book.

**URL**: `/FBV_list`  
**Methods**: `GET`, `POST`  
**Response**:

- `GET`:
```json
[
    // List of active books
]
```

- `POST`:
```json
{
    // Newly created book data
}
```

### 4. Retrieve, Update, and Delete Book by ID (Function-Based View)
This endpoint retrieves, updates, and deletes a book by its ID.

**URL**: `/FBV_with_PK/<pk>`  
**Methods**: `GET`, `PUT`, `DELETE`  
**Response**:

- `GET`:
```json
{
    // Book data with the given ID
}
```

- `PUT`:
```json
{
    // Updated book data
}
```

- `DELETE`: `204 No Content`

### 5. Retrieve Book by ID (Function-Based View)
This endpoint retrieves a book by its ID.

**URL**: `/get_book_with_pk/<pk>`  
**Method**: `GET`  
**Response**:
```json
{
    // Book data with the given ID
}
```

### 6. Update Book by ID (Function-Based View)
This endpoint updates a book by its ID.

**URL**: `/update_book/<pk>`  
**Method**: `PUT`  
**Response**:
```json
{
    // Updated book data
}
```

### 7. Delete Book by ID (Function-Based View)
This endpoint deletes a book by its ID.

**URL**: `/delete_book/<pk>`  
**Method**: `DELETE`  
**Response**: `204 No Content`

### 8. List and Create Books (Class-Based View)
This endpoint lists all active books and allows the creation of a new book using class-based views.

**URL**: `/CBV_List`  
**Methods**: `GET`, `POST`  
**Response**:

- `GET`:
```json
[
    // List of active books
]
```

- `POST`:
```json
{
    // Newly created book data
}
```

### 9. Retrieve, Update, and Delete Book by ID (Class-Based View)
This endpoint retrieves, updates, and deletes a book by its ID using class-based views.

**URL**: `/CBV_pk/<pk>`  
**Methods**: `GET`, `PUT`, `DELETE`  
**Response**:

- `GET`:
```json
{
    // Book data with the given ID
}
```

- `PUT`:
```json
{
    // Updated book data
}
```

- `DELETE`: `204 No Content`

### 10. List and Create Books (Mixins)
This endpoint lists all active books and allows the creation of a new book using mixins.

**URL**: `/Mixins_List`  
**Methods**: `GET`, `POST`  
**Response**:

- `GET`:
```json
[
    // List of active books
]
```

- `POST`:
```json
{
    // Newly created book data
}
```

### 11. Retrieve, Update, and Delete Book by ID (Mixins)
This endpoint retrieves, updates, and deletes a book by its ID using mixins.

**URL**: `/Mixins_Pk/<pk>`  
**Methods**: `GET`, `PUT`, `DELETE`  
**Response**:

- `GET`:
```json
{
    // Book data with the given ID
}
```

- `PUT`:
```json
{
    // Updated book data
}
```

- `DELETE`: `204 No Content`

### 12. List and Create Books (Generics)
This endpoint lists all active books and allows the creation of a new book using generics.

**URL**: `/Generics_List`  
**Methods**: `GET`, `POST`  
**Response**:

- `GET`:
```json
[
    // List of active books
]
```

- `POST`:
```json
{
    // Newly created book data
}
```

### 13. Retrieve, Update, and Delete Book by ID (Generics)
This endpoint retrieves, updates, and deletes a book by its ID using generics.

**URL**: `/Generics_by_PK/<pk>`  
**Methods**: `GET`, `PUT`, `DELETE`  
**Response**:

- `GET`:
```json
{
    // Book data with the given ID
}
```

- `PUT`:
```json
{
    // Updated book data
}
```

- `DELETE`: `204 No Content`

### 14. Viewsets for Books
This endpoint provides all CRUD operations for books using viewsets.

**URL**: `/Viewsets_books`  
**Methods**: `GET`, `POST`, `PUT`, `DELETE`  
**Response**:

- `GET`:
```json
[
    // List of active books
]
```

- `POST`:
```json
{
    // Newly created book data
}
```

- `PUT`:
```json
{
    // Updated book data
}
```

- `DELETE`: `204 No Content`

### 15. Viewsets for Categories
This endpoint provides all CRUD operations for categories using viewsets.

**URL**: `/Viewsets_Category`  
**Methods**: `GET`, `POST`, `PUT`, `DELETE`  
**Response**:

- `GET`:
```json
[
    // List of categories
]
```

- `POST`:
```json
{
    // Newly created category data
}
```

- `PUT`:
```json
{
    // Updated category data
}
```

- `DELETE`: `204 No Content`

### 16. Search Book
This endpoint searches for a book by its title and ID.

**URL**: `/search_book`  
**Method**: `GET`  
**Response**:
```json
[
    // List of books matching the search criteria
]
```

### 17. Post Author Editor
This endpoint retrieves, updates, and deletes a post by its ID with author permissions.

**URL**: `/Post_pk/<pk>`  
**Methods**: `GET`, `PUT`, `DELETE`  
**Response**:

- `GET`:
```json
{
    // Post data with the given ID
}
```

- `PUT`:
```json
{
    // Updated post data
}
```

- `DELETE`: `204 No Content`

## Authentication and Permissions
- Some endpoints require `TokenAuthentication`.
- The `Post_pk` endpoint requires `IsAuthorOrReadOnly` permission.
