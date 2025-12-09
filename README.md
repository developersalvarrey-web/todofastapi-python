# 🐍 FastAPI Todo API  
### Python + FastAPI + SQLAlchemy + Uvicorn

A clean, modern and lightweight REST API built with **FastAPI**.  
This backend powers the Todo application and provides a fully functional CRUD system for managing tasks.

Designed with a clean project structure, database models, Pydantic schemas, and automatic interactive documentation using Swagger UI.

Perfect for full-stack portfolio projects.

---

# 🚀 Features

- ⚡ **FastAPI** (extremely fast Python web framework)
- 🗄 **SQLAlchemy** ORM
- 💾 **SQLite** database (lightweight & zero-config)
- 🔄 Full CRUD for tasks:
  - Create
  - Read (list)
  - Update
  - Delete
- 🔌 Clear separation:
  - Models
  - Schemas
  - Database engine
  - Routes
- 🧪 Automatic Swagger documentation
- 🟢 Fully compatible with the React client (multi-backend client)
- ⏱ Auto-reload with `uvicorn --reload`

---

# 🧱 Technologies Used

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

---

# 📂 Project Structure


python-todo-api/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI application
│ ├── database.py # DB engine + session
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ └── routes.py # Task CRUD endpoints
├── venv/ # Virtual environment (optional)
├── requirements.txt
└── README.md
 

---

# ⚙️ Installation

## 1️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
Activate it:

Windows:
 
venv\Scripts\activate
Mac / Linux:
 
source venv/bin/activate
2️⃣ Install dependencies
 
pip install -r requirements.txt
Or manually:

 
pip install fastapi uvicorn sqlalchemy
▶️ Run the API
 
uvicorn app.main:app --reload
The API will run at:

cpp
  
http://127.0.0.1:8000
📘 Swagger Documentation
Visit:

 
http://127.0.0.1:8000/docs
Or ReDoc:

 
http://127.0.0.1:8000/redoc
Interactive documentation is generated automatically by FastAPI.

🔗 API Endpoints
Get all tasks
 
GET /tasks
Create a new task
 
POST /tasks
Update a task
 
PUT /tasks/{id}
Delete a task
 
DELETE /tasks/{id}
🧠 Data Model
SQLAlchemy Model
id (int)

title (string)

description (string | nullable)

is_completed (boolean)

created_at (datetime UTC)

due_date (datetime | nullable)

Pydantic Schemas
TaskBase

TaskCreate

TaskUpdate

Task

TaskList

All responses follow snake_case naming for perfect compatibility with the multi-backend React client.

🖥 Frontend Integration
This backend is fully compatible with the multi-backend React client, which toggles between:

ASP.NET Core API

FastAPI Python API

No changes are required on the API side.

📌 SQL Database
The project uses SQLite by default and creates todos.db on first run.

If you prefer PostgreSQL or MySQL, simply update the SQLALCHEMY_DATABASE_URL inside database.py.

👨‍💻 Author
Cristian Gómez
Full Stack Developer (Python + .NET + React)
Building modern and scalable full stack portfolio applications.
