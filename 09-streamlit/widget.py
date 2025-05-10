import streamlit as st
import pandas as pd

st.title("Streamlit text input")
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}!")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is {age} years old.")


options = ["Python", "Java", "C++"]
selected_option = st.selectbox("Select a programming language", options)
st.write(f"You selected: {selected_option}")

data = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [5, 6, 7, 8],
    "Column 3": [9, 10, 11, 12]
})

st.write(data)

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write("Uploaded DataFrame:")
    st.write(df)