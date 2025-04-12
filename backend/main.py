from fastapi import Depends, HTTPException, FastAPI, Response
from schemas.TaskSchema import Task, TaskCreate, TaskUpdate
from schemas.UserSchema import User
from database import init_db
from repositories import task_repository, user_repository
from pydantic import ValidationError
from auth import get_current_user, create_access_token, authenticate_user
from utils.auth import validate_username
from datetime import timedelta

app = FastAPI() 
init_db()

@app.get("/")
async def read_root():
    return {"message": "Добро пожаловать в FastAPI!"}

@app.post("/register")
async def register_user(user: User):
    return user_repository.register_user(user)

@app.post("/login")
async def login(username: str, password: str, response: Response):
    try:
        # Валидация имени пользователя
        validate_username(username)
        
        user = authenticate_user(username, password)
        if not user:
            raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")
        
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": user["username"]}, expires_delta=access_token_expires
        )
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            max_age=1800,
            expires=1800,
            secure=False,
        )
        return {"message": "Вы успешно вошли"}
    except ValidationError as e:
        # Преобразуем наши кастомные исключения в HTTP-исключения
        raise HTTPException(status_code=400, detail=e.message)

@app.get("/tasks")
async def get_tasks(current_user: dict = Depends(get_current_user)):
    return task_repository.get_all_tasks(current_user["id"])

@app.post("/task")
async def create_task(task: TaskCreate, current_user: dict = Depends(get_current_user)):
    return task_repository.create_task(task, current_user["id"])

@app.put("/task/{task_id}", response_model=Task)
async def update_task(task_id: str, task_update: TaskUpdate, current_user: dict = Depends(get_current_user)):
    return task_repository.update_task(task_id, task_update, current_user["id"])

@app.delete("/task/{task_id}")
async def delete_task(task_id: str, current_user: dict = Depends(get_current_user)):
    return task_repository.delete_task(task_id, current_user["id"])