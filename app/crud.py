from typing import List, Optional
from sqlalchemy.orm import Session
from . import models, schemas

def get_tasks(db: Session) -> List[models.Task]:
    return db.query(models.Task).order_by(models.Task.created_at.desc()).all()

def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task_in: schemas.TaskCreate) -> models.Task:
    task = models.Task(
        title=task_in.title,
        description=task_in.description,
        due_date=task_in.due_date,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task(
    db: Session, task_db: models.Task, task_in: schemas.TaskUpdate
) -> models.Task:
    task_db.title = task_in.title
    task_db.description = task_in.description
    if task_in.is_completed is not None:
        task_db.is_completed = task_in.is_completed
    task_db.due_date = task_in.due_date
    db.commit()
    db.refresh(task_db)
    return task_db

def delete_task(db: Session, task_db: models.Task) -> None:
    db.delete(task_db)
    db.commit()
