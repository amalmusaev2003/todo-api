import streamlit as st
import requests
from requests.exceptions import RequestException

# Настройка URL API
API_URL = "http://localhost:8000"  # Измените, если ваш FastAPI работает на другом порту

def login_user(username, password):
    """Попытка входа пользователя через API"""
    try:
        response = requests.post(
            f"{API_URL}/login",
            params={"username": username, "password": password}
        )
        
        if response.status_code == 200:
            # Сохранение cookies из ответа
            st.session_state.cookies = response.cookies
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.error_message = ""
            return True
        else:
            error_detail = response.json().get("detail", "Неизвестная ошибка")
            st.session_state.error_message = f"Ошибка входа: {error_detail}"
            return False
    except RequestException as e:
        st.session_state.error_message = f"Ошибка соединения: {str(e)}"
        return False

def register_user(username, password):
    """Регистрация нового пользователя через API"""
    try:
        response = requests.post(
            f"{API_URL}/register",
            json={"username": username, "password": password}
        )
        
        if response.status_code == 200:
            st.session_state.error_message = ""
            return True, "Регистрация успешна! Теперь вы можете войти."
        else:
            error_detail = response.json().get("detail", "Неизвестная ошибка")
            st.session_state.error_message = f"Ошибка регистрации: {error_detail}"
            return False, st.session_state.error_message
    except RequestException as e:
        st.session_state.error_message = f"Ошибка соединения: {str(e)}"
        return False, st.session_state.error_message
