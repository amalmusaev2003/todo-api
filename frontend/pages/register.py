import streamlit as st
from utils.api import register_user

def show_register_page():
    """Отображение страницы регистрации"""
    st.title("Регистрация в Todo App")
    
    # Форма регистрации
    with st.form("register_form"):
        username = st.text_input("Имя пользователя")
        password = st.text_input("Пароль", type="password")
        confirm_password = st.text_input("Подтвердите пароль", type="password")
        submit_button = st.form_submit_button("Зарегистрироваться")
        
        if submit_button:
            if not username or not password:
                st.error("Пожалуйста, заполните все поля")
            elif password != confirm_password:
                st.error("Пароли не совпадают")
            else:
                success, message = register_user(username, password)
                if success:
                    st.success(message)
                    st.session_state.page = "login"
    
    # Ссылка на вход
    st.write("Уже есть аккаунт?")
    if st.button("Войти"):
        st.session_state.page = "login"
    
    # Отображение сообщения об ошибке, если есть
    if st.session_state.error_message:
        st.error(st.session_state.error_message)