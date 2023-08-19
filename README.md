# GraphQL Backend Application with Flask

A simple Python backend application using Flask, SQLAlchemy, Graphene, Flask-Login, and Flask-Principal to demonstrate GraphQL with CRUD functionality and authentication & authorization for a `Book` model.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo-link/graphql-flask-backend.git
   cd graphql-flask-backend
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install Flask Flask-GraphQL Flask-SQLAlchemy graphene graphene-sqlalchemy Flask-Login Flask-Principal
   ```

## Usage

### Models

The application supports the following models:

- `Book` with fields:
  - `id`: Integer, Primary Key
  - `title`: String
  - `author`: String

- `User` for authentication with fields:
  - `id`: Integer, Primary Key
  - `username`: String, Unique
  - `password`: String (hashed)
  - `role`: String (e.g., 'admin')

### GraphQL Operations

- **Create a Book**:
  ```graphql
  mutation {
    createBook(title: "Sample Book", author: "John Doe") {
      book {
        id
        title
        author
      }
    }
  }
  ```

- **Update a Book**:
  ```graphql
  mutation {
    updateBook(id: 1, title: "Updated Book") {
      book {
        id
        title
        author
      }
    }
  }
  ```

- **Delete a Book**:
  ```graphql
  mutation {
    deleteBook(id: 1) {
      success
    }
  }
  ```

- **Fetch All Books**:
  ```graphql
  {
    allBooks {
      edges {
        node {
          id
          title
          author
        }
      }
    }
  }
  ```

- **Fetch a Book by Title**:
  ```graphql
  {
    bookByTitle(title: "Sample Book") {
      id
      title
      author
    }
  }
  ```

## Authentication

- **Login**:
  Users can log in through the `/login` route. Only logged-in users with the 'admin' role can create books.

## Endpoints

- `/graphql`: The main GraphQL endpoint. Use this to perform all CRUD operations. You can also access the GraphiQL interface here for testing and documentation.
- `/login`: Endpoint for user login.

## Running the Application

1. Execute the Python script:
   ```bash
   python app.py
   ```

2. Visit `http://localhost:5000/graphql` in your browser to access the GraphiQL interface and test the CRUD operations.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
