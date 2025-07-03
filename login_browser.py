import streamlit as st

# Define credentials
USERNAME = "admin"
PASSWORD = "1234"

st.title("🔐 Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success(f"✅ Welcome, {username}!")
    else:
        st.error("❌ Invalid username or password.")
