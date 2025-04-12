import streamlit as st

def initialize_session():
    """Инициализация всех переменных состояния сессии"""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "error_message" not in st.session_state:
        st.session_state.error_message = ""
    if "success_message" not in st.session_state:
        st.session_state.success_message = ""
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "cookies" not in st.session_state:
        st.session_state.cookies = None
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

def logout():
    """Выход текущего пользователя из системы"""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.cookies = None
    st.session_state.error_message = ""
    st.session_state.success_message = ""
    st.session_state.page = "login"
    if "tasks" in st.session_state:
        st.session_state.tasks = []

def set_error(message):
    """Установка сообщения об ошибке в состоянии сессии"""
    st.session_state.error_message = message
    st.session_state.success_message = ""  # Очистка любого сообщения об успехе

def clear_error():
    """Очистка сообщения об ошибке в состоянии сессии"""
    st.session_state.error_message = ""

def set_success(message):
    """Установка сообщения об успехе в состоянии сессии"""
    st.session_state.success_message = message
    st.session_state.error_message = ""  # Очистка любого сообщения об ошибке

def clear_success():
    """Очистка сообщения об успехе в состоянии сессии"""
    st.session_state.success_message = ""

def navigate_to(page):
    """Переход на определенную страницу"""
    st.session_state.page = page

def is_logged_in():
    """Проверка, вошел ли пользователь в систему"""
    return st.session_state.logged_in