# Flask Blog Application

A full-featured blog application built with Flask, providing a RESTful API backend and a simple, intuitive frontend. This application allows users to manage blog posts and comments, showcasing backend development skills, problem-solving abilities, and familiarity with building RESTful APIs.

## Features

- **Blog Posts Management**: Users can create, read, update, and delete blog posts.
- **Comments**: Users can add comments to blog posts, enhancing interaction.
- **RESTful API**: Backend API follows RESTful principles, making it easy to understand and use.
- **Frontend**: Includes a basic frontend interface to interact with the blog posts and comments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/blogapp.git
    cd blogapp
    ```

2. **Set up a virtual environment** (optional but recommended)

    - **Windows:**

      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

    - **macOS/Linux:**

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize the database**

    ```bash
    python
    >>> from app import db
    >>> db.create_all()
    ```

5. **Run the application**

    ```bash
    flask run
    ```

    The application will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

Refer to [DOCUMENTATION.md](DOCUMENTATION.md) for detailed API documentation, including endpoints for managing blog posts and comments.


