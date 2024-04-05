Below is the `DOCUMENTATION.md` that includes detailed instructions on how to use the API through the command line on Windows/Mac, as well as guidance on operating the frontend. This comprehensive document aims to provide all the necessary information for both backend and frontend usage of the blog application.

---

# Blog Application Documentation

## Overview

This documentation covers the usage of the Blog Application, which offers a RESTful API for managing blog posts and comments. It includes instructions for setting up the application, utilizing the API, and interacting with the application's frontend.

## Table of Contents

- [Setting Up the Application](#setting-up-the-application)
- [API Endpoint Guide](#api-endpoint-guide)
  - [Blog Posts](#blog-posts)
  - [Comments](#comments)
- [Using the API from the Command Line](#using-the-api-from-the-command-line)
- [Interacting with the Frontend](#interacting-with-the-frontend)

## Setting Up the Application

Please refer to the `README.md` for initial setup and running instructions. Ensure you have Python and all necessary dependencies installed before proceeding.

## API Endpoint Guide

The application's backend functionality is exposed through a series of RESTful endpoints. Here’s how to interact with them:

### Blog Posts

- **Retrieve All Posts** (`GET /posts`): Fetches a list of all blog posts.
- **Retrieve a Specific Post** (`GET /posts/{id}`): Fetches a specific blog post by its ID.
- **Create a New Post** (`POST /posts`): Creates a new blog post with a title, content, and author.
- **Update an Existing Post** (`PUT /posts/{id}`): Updates an existing blog post by ID.
- **Delete a Post** (`DELETE /posts/{id}`): Deletes a blog post by ID.

### Comments

- **Retrieve Comments for a Post** (`GET /posts/{postId}/comments`): Fetches all comments for a specific blog post.
- **Add a Comment to a Post** (`POST /posts/{postId}/comments`): Adds a new comment to a specific blog post.

## Using the API from the Command Line

You can interact with the API using `curl` on Mac/Linux or PowerShell on Windows. Here are examples for each endpoint:

### Retrieve All Posts

- **curl**:
  ```sh
  curl http://127.0.0.1:5000/posts
  ```
- **PowerShell**:
  ```powershell
  Invoke-RestMethod -Uri "http://127.0.0.1:5000/posts" -Method Get
  ```

### Create a New Post

- **curl**:
  ```sh
  curl -X POST http://127.0.0.1:5000/posts -H "Content-Type: application/json" -d "{\"title\":\"New Post\", \"content\":\"Post content\", \"author\":\"Author\"}"
  ```
- **PowerShell**:
  ```powershell
  $body = @{
      title = "New Post"
      content = "Post content"
      author = "Author"
  } | ConvertTo-Json
  Invoke-RestMethod -Uri "http://127.0.0.1:5000/posts" -Method Post -Body $body -ContentType "application/json"
  ```

_(Continue with similar examples for other endpoints.)_

## Interacting with the Frontend

The frontend provides a web interface to interact with the blog. After starting the application, visit `http://127.0.0.1:5000/` in your web browser. The homepage displays all blog posts, and you can navigate to individual posts to see comments and add new ones. Use the provided forms to create new posts and comments.

### Creating a Post

- Navigate to the homepage.
- Fill out the form with the title, author, and content of your post.
- Submit the form to create a new post.

### Adding a Comment

- Click on a post to view its details.
- Use the comment form at the bottom of the post page to add a new comment.

For detailed API usage, refer to the API Endpoint Guide section. 
