
```markdown
# API Endpoint Documentation

## Blog Application API

This document outlines the API endpoints available in the Blog Application, providing functionalities to manage blog posts and comments.

### Base URL

All URLs referenced in the documentation have the base path `http://127.0.0.1:5000/`

## Blog Posts

### Retrieve All Posts

- **GET** `/posts`
- Retrieves a list of all blog posts.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "title": "Post Title",
      "content": "Post content here...",
      "author": "Author Name"
    }
  ]
  ```

### Retrieve a Specific Post

- **GET** `/posts/{id}`
- Retrieves a specific blog post by its ID.
- **Parameters**:
  - `id`: The unique identifier for the blog post.
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Post Title",
    "content": "Post content here...",
    "author": "Author Name"
  }
  ```

### Create a New Post

- **POST** `/posts`
- Creates a new blog post.
- **Request Body**:
  ```json
  {
    "title": "New Post Title",
    "content": "Content of the new post.",
    "author": "Author's Name"
  }
  ```
- **Response**:
  ```json
  {
    "id": 2,
    "title": "New Post Title",
    "content": "Content of the new post.",
    "author": "Author's Name"
  }
  ```

### Update an Existing Post

- **PUT** `/posts/{id}`
- Updates an existing blog post.
- **Parameters**:
  - `id`: The unique identifier for the blog post to update.
- **Request Body**:
  ```json
  {
    "title": "Updated Post Title",
    "content": "Updated content of the post.",
    "author": "Author's Name"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Updated Post Title",
    "content": "Updated content of the post.",
    "author": "Author's Name"
  }
  ```

### Delete a Post

- **DELETE** `/posts/{id}`
- Deletes a blog post by its ID.
- **Parameters**:
  - `id`: The unique identifier for the blog post to delete.
- **Response**: A success message indicating the post has been deleted.

## Comments

### Retrieve Comments for a Post

- **GET** `/posts/{postId}/comments`
- Retrieves all comments for a specific blog post.
- **Parameters**:
  - `postId`: The unique identifier of the blog post.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "postId": 1,
      "content": "Comment content here...",
      "author": "Commenter Name"
    }
  ]
  ```

### Add a Comment to a Post

- **POST** `/posts/{postId}/comments`
- Adds a new comment to a specific blog post.
- **Parameters**:
  - `postId`: The unique identifier of the blog post.
- **Request Body**:
  ```json
  {
    "content": "New comment content.",
    "author": "Commenter's Name"
  }
  ```
- **Response**:
  ```json
  {
    "id": 2,
    "postId": 1,
    "content": "New comment content.",
    "author": "Commenter's Name"
  }
  ```
```

