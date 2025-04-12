# schemas/TaskSchema.py
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False

class Task(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None