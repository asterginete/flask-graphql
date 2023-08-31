graphql-flask-backend/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── user.py
│   │   ├── notification.py
│   │   ├── rate_limit.py
│   │   └── social_auth.py
│   │
│   ├── schema/
│   │   ├── __init__.py
│   │   ├── inputs/
│   │   │   ├── __init__.py
│   │   │   ├── book_input.py
│   │   │   └── user_input.py
│   │   ├── mutations/
│   │   │   ├── __init__.py
│   │   │   ├── book.py
│   │   │   ├── user.py
│   │   │   └── notification.py
│   │   ├── queries/
│   │   │   ├── __init__.py
│   │   │   ├── book.py
│   │   │   └── user.py
│   │   └── schema.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── auth.py
│   │   └── notifications.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── email_service.py
│   │   └── rate_limit_service.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── helpers.py
│   │
│   └── templates/
│       ├── login.html
│       ├── register.html
│       └── reset_password.html
│
├── migrations/
│
├── tests/
│   ├── __init__.py
│   ├── test_books.py
│   ├── test_users.py
│   └── test_notifications.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── venv/
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
