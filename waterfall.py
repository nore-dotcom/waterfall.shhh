import streamlit as st
import datetime

# --- App Title ---
st.set_page_config(page_title="Simple Streamlit App", page_icon="🌟", layout="centered")
st.title("🌟 Welcome to My Streamlit App")
st.write("A simple interactive demo with widgets and layout.")

# --- Sidebar ---
st.sidebar.header("⚙️ Settings")
theme = st.sidebar.radio("Choose a theme:", ["Light", "Dark", "Colorful"])
show_info = st.sidebar.checkbox("Show App Info")

if show_info:
    st.sidebar.success("This app demonstrates Streamlit basics in one page!")

# --- User Input Section ---
st.subheader("👤 User Information")
name = st.text_input("Enter your name")
age = st.slider("Select your age", 1, 100, 18)
dob = st.date_input("Pick your birthday", datetime.date(2000, 1, 1))

if name:
    st.success(f"Hello, {name}! 🎉 You are {age} years old.")
    st.write(f"Your birthday is on **{dob.strftime('%B %d, %Y')}**.")

# --- Fun Section ---
st.subheader("🎲 Just for Fun")
number = st.number_input("Pick a number", 1, 10, 5)
if st.button("Double It!"):
    st.write(f"Your number doubled is 👉 {number * 2}")

# --- Data Display ---
st.subheader("📊 Sample Data Table")
import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "London", "Paris", "Tokyo"]
})
st.dataframe(df)
