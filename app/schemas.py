from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    is_completed: Optional[bool] = None

class TaskRead(TaskBase):
    id: int
    is_completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
