import streamlit as st
from utils.api import login_user

def show_login_page():
    """Display the login page"""
    st.title("Вход в Todo App")
    
    # Login form
    with st.form("login_form"):
        username = st.text_input("Имя пользователя")
        password = st.text_input("Пароль", type="password")
        submit_button = st.form_submit_button("Войти")
        
        if submit_button:
            if not username or not password:
                st.error("Пожалуйста, введите имя пользователя и пароль")
            else:
                login_user(username, password)
    
    # Registration link
    st.write("Нет аккаунта?")
    if st.button("Зарегистрироваться"):
        st.session_state.page = "register"
    
    # Display error message if any
    if st.session_state.error_message:
        st.error(st.session_state.error_message)