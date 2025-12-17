import streamlit as st
import pandas as pd
from app.db import get_connection 
from app.users import set_user, get_one_user, verify_password
from app.users import hash_password
from app.users import is_valid_hash
conn = get_connection()
st.title ("Welcome to the Home Page")
st.write ("This is the home page of the Cyber Incidents Dashboard Application.")
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ""


tab_log_in, tab_registration = st.tabs(["Log In", "Registration"]) 
with tab_log_in:
    st.header("Log In")

    login_username = st.text_input("Username",key="login_username")
    login_password = st.text_input("Password", type="password",key="login_password")
    
    if st.button("Log in"):
        user = get_one_user(conn, login_username)
        if user is None:
            st.error("Username not found. Please register first.")
        else:
            # user = (id, username, password_hash, role, ...)
            # Access by index instead of unpacking
            user_hash = user[2]  # password_hash is at index 2
            if verify_password(user_hash, login_password):
                st.session_state['logged_in'] = True
                st.success("You are now logged in!")
                st.session_state['username'] = login_username
                st.switch_page('pages/Dashboard.py')
            else:
                st.error("Invalid password.")


with tab_registration:
    st.header("User Registration")
    register_user = st.text_input("Choose a Username",key="register_username")
    register_password = st.text_input("Choose a Password", type="password",key="register_password")
    
    if st.button("Register"):
        try:
            hashed_pwd = hash_password(register_password)
            set_user(conn, register_user, hashed_pwd)
            st.success("Registration successful! You can now log in.")
        except Exception as e:
            st.error(f"Registration failed: {str(e)}")