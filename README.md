# Library Management System (LMS) API

This project is a backend API for a Library Management System, built using Django and Django REST Framework (DRF). It handles the core functionality you’d expect in a library system—user authentication, book management, borrowing records, and reviews.

## What's inside?

The API is structured into separate apps to keep things modular and easy to maintain:
- **`users`**: Manages custom user authentication and JWT-based login.
- **`books`**: Handles everything related to books (add, update, view, etc.).
- **`borrow`**: Keeps track of borrowed books, due dates, and returns.
- **`reviews`**: Lets users rate and review books they’ve read.

## Tech Stack
- **Framework**: Django & Django REST Framework
- **Auth**: Simple JWT (JSON Web Tokens)
- **Database**: SQLite (default, but easy to swap out)
- **API Docs**: drf-yasg (Swagger/ReDoc)

## Getting Started

If you want to spin this up locally, just follow these steps:

1. **Clone the repo** (if you haven't already):
   ```bash
   git clone <your-repo-url>
   cd LMS
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** to set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Exploring the API

Once the server is running (usually at `http://127.0.0.1:8000/`), you can check out the interactive API documentation. We use Swagger, which makes testing endpoints super easy.

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

For protected endpoints, you’ll need a JWT token. After logging in, just paste the token into Swagger’s “Authorize” button—it will handle the Bearer prefix automatically.


