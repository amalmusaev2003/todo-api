from fastapi import HTTPException
from schemas.UserSchema import User
from database import get_db_cursor
from passlib.context import CryptContext
from utils.auth import validate_username, validate_password
from exceptions import UserAlreadyExistsError, ValidationError

# Настройка хеширования
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(user: User):
    try:
        # Валидация имени пользователя и пароля
        validate_username(user.username)
        validate_password(user.password)
        
        # Проверяем, что пользователь с таким именем не существует
        with get_db_cursor() as cursor:
            cursor.execute("SELECT id FROM users WHERE username = ?", (user.username,))
            if cursor.fetchone():
                raise UserAlreadyExistsError()
        
        # Хешируем пароль
        hashed_password = pwd_context.hash(user.password)
        with get_db_cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", 
                (user.username, hashed_password)
            )
            return {"message": "Пользователь зарегистрирован"}
    except ValidationError as e:
        # Преобразуем наши кастомные исключения в HTTP-исключения
        raise HTTPException(status_code=400, detail=str(e))

def get_user(username: str):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "username": row[1], "password": row[2]}
    return None