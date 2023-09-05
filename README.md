# GraphQL Flask Backend Application

A comprehensive Python backend application using Flask, SQLAlchemy, and Graphene to demonstrate GraphQL with CRUD functionality, authentication, rate limiting, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **GraphQL API**: Perform CRUD operations on books and users.
- **Authentication**: Secure user registration and login using password hashing.
- **Social Authentication**: Allow users to log in using third-party services.
- **Rate Limiting**: Limit the number of API requests per IP to prevent abuse.
- **Notifications**: Send and manage user notifications.
- **Password Reset**: Generate tokens for password reset functionality.
- **Email Service**: Utility to send emails (e.g., for password reset).
- **Validators**: Utility functions to validate email and password formats.
- **Helpers**: Utility functions for common tasks like generating random strings.

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
   pip install -r requirements.txt
   ```

## Usage

### Models

- **Book**: Contains fields like `id`, `title`, and `author`.
- **User**: Contains fields like `id`, `username`, `email`, and `role`.
- **Notification**: Manages user notifications.
- **APIRateLimit**: Tracks and enforces rate limits for different IP addresses.
- **UserSocialAuth**: Stores authentication details for third-party services.
- **PasswordResetToken**: Manages tokens for password reset functionality.

### GraphQL Operations

Refer to the individual GraphQL files for detailed operations, including creating, updating, deleting, and querying books and users.

## Endpoints

- `/graphql`: The main GraphQL endpoint. Use this to perform all CRUD operations. You can also access the GraphiQL interface here for testing and documentation.

## Running the Application

1. **Set up the database**:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

2. **Execute the Python script**:
   ```bash
   python run.py
   ```

3. **Visit**:
   Open `http://localhost:5000/graphql` in your browser to access the GraphiQL interface and test the CRUD operations.

## Testing

Tests are located in the `tests/` directory. To run them, use:

```bash
pytest
```

## Contributing

1. Fork the repository.
2. Create a new branch for your features or bug fixes.
3. Commit your changes and push to your fork.
4. Open a pull request from your fork to the main repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.