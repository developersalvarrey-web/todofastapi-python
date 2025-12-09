from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import SessionLocal, engine

# Create DB tables
models.Task.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API (Python)",
    description="Simple Todo API built with FastAPI + SQLAlchemy, mirroring the .NET version.",
    version="1.0.0",
)

# CORS (to talk to your React client on http://localhost:5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency: get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks", response_model=List[schemas.TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}", response_model=schemas.TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task

@app.post("/tasks", response_model=schemas.TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task_in)

@app.put("/tasks/{task_id}", response_model=schemas.TaskRead)
def update_task(
    task_id: int, task_in: schemas.TaskUpdate, db: Session = Depends(get_db)
):
    task_db = crud.get_task(db, task_id)
    if not task_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return crud.update_task(db, task_db, task_in)

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_db = crud.get_task(db, task_id)
    if not task_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    crud.delete_task(db, task_db)
    return None
