from fastapi import HTTPException
from database import get_db_cursor
from schemas.TaskSchema import Task, TaskCreate, TaskUpdate
from uuid import uuid4

def get_all_tasks(user_id: int):
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT id, title, description, is_completed FROM tasks WHERE user_id = ?",
            (user_id,)
        )
        rows = cursor.fetchall()
        return [
            {"id": row[0], "title": row[1], "description": row[2], "is_completed": bool(row[3])}
            for row in rows
        ]

def create_task(task: TaskCreate, user_id: int):
    task_id = str(uuid4())  # Генерируем UUID
    with get_db_cursor() as cursor:
        cursor.execute(
            "INSERT INTO tasks (id, title, description, is_completed, user_id) VALUES (?, ?, ?, ?, ?)",
            (task_id, task.title, task.description, task.is_completed, user_id)
        )
        return {"message": "Задача успешно добавлена", "id": task_id}

def get_task_by_id(task_id: str, user_id: int) -> Task:
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT id, title, description, is_completed FROM tasks WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Задача не найдена или не принадлежит вам")
        return Task(title=row[1], description=row[2], is_completed=bool(row[3]))

def update_task(task_id: str, task_update: TaskUpdate, user_id: int):
    task = get_task_by_id(task_id, user_id)  # Проверяем, что задача принадлежит пользователю
    new_title = task_update.title if task_update.title is not None else task.title
    new_description = task_update.description if task_update.description is not None else task.description
    new_is_completed = task_update.is_completed if task_update.is_completed is not None else task.is_completed

    with get_db_cursor() as cursor:
        cursor.execute(
            "UPDATE tasks SET title = ?, description = ?, is_completed = ? WHERE user_id = ?",
            (new_title, new_description, new_is_completed, user_id)
        )
        return Task(title=new_title, description=new_description, is_completed=new_is_completed)

def delete_task(task_id: str, user_id: int):
    with get_db_cursor() as cursor:
        cursor.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, user_id))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Задача не найдена или не принадлежит вам")
        return {"message": "Задача успешно удалена"}