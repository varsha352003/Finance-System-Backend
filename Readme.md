# Python Finance Tracking Backend

A clean and modular **FastAPI-based finance tracking backend** built to manage financial records, analytics, and role-based user handling.

This project allows users to:
- create and manage income/expense transactions
- filter records by category and type
- view financial summaries
- manage users and roles
- store data persistently using SQLite

The backend is designed with a **modular architecture** using separate files for models, schemas, routes, database setup, and analytics services.

---

# Features

## Financial Records CRUD
Supports complete transaction management:
- Create transactions
- View all transactions
- View a single transaction
- Update transactions
- Delete transactions

## Record Filtering
Transactions can be filtered using:
- category
- type

## Summary and Analytics APIs
Provides useful financial insights:
- Total income
- Total expense
- Current balance
- Category-wise breakdown
- Monthly summary
- Recent activity

## User and Role Handling
Supports basic user management:
- Create users
- Get all users
- Get user by ID
- Update user role

Supported roles:
- viewer
- analyst
- admin

## Input Validation and Error Handling
Implemented using **Pydantic schemas** and **HTTP exceptions**.

Includes:
- required field validation
- datatype validation
- invalid ID handling
- 404 errors

## Database Persistence
Uses:
- SQLite
- SQLAlchemy ORM

Database file:
- `finance_system.db`

---

# Project Structure

```text
finance_backend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── routes/
│   ├── users.py
│   ├── transactions.py
│   └── summary.py
│
├── services/
│   └── analytics.py
│
└── finance_system.db
```

---

# Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# API Endpoints

## User Routes
- `POST /users`
- `GET /users`
- `GET /users/{user_id}`
- `PATCH /users/{user_id}/role`

## Transaction Routes
- `POST /transactions`
- `GET /transactions`
- `GET /transactions/{transaction_id}`
- `PUT /transactions/{transaction_id}`
- `DELETE /transactions/{transaction_id}`
- `GET /transactions/filter`

## Summary Routes
- `GET /summary`
- `GET /summary/category`
- `GET /summary/monthly`
- `GET /summary/recent`

---

# How to Run

## 1) Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## 2) Start the server
```bash
uvicorn main:app --reload
```

## 3) Open Swagger docs
```text
http://127.0.0.1:8000/docs
```

---

# Sample Use Case

Example transaction:
- Salary → ₹50,000
- Food → ₹2,000
- Travel → ₹1,000

Summary output:
- Total income → ₹50,000
- Total expense → ₹3,000
- Balance → ₹47,000

---

# Design Decisions

The project follows **separation of concerns**:
- `models.py` → database tables
- `schemas.py` → request/response validation
- `routes/` → API endpoints
- `services/analytics.py` → business logic and calculations
- `database.py` → database setup and sessions
- `main.py` → application startup and route registration

This structure improves:
- readability
- maintainability
- scalability

---

# Future Improvements

Possible enhancements:
- JWT authentication
- stricter role-based access control
- date-based filtering
- pagination
- CSV export
- Docker deployment
- unit tests

---

# Author

**Varsha Bahuguna**

Built as a backend assessment project to demonstrate:
- Python backend development
- API design
- database handling
- business logic
- clean architecture
- validation and error handling

