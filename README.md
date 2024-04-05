# Blog Application

A Flask-based web application designed to manage blog posts and comments through a RESTful API. This application demonstrates backend development skills, problem-solving abilities, and familiarity with RESTful API design.

## Features

- Manage blog posts (Create, Read, Update, Delete)
- Add comments to posts
- RESTful API architecture

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/<yourusername>/blogapp.git
cd blogapp
pip install -r requirements.txt

#Initialize Database-

python
>>> from app import db
>>> db.create_all()


## Run the Server

flask run
Access the application at http://127.0.0.1:5000/
