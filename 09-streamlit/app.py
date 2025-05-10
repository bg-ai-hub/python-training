import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Streamlit Application")

## Display simple text
st.write("This is a simple text.")

df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [5, 6, 7, 8],
    "Column 3": [9, 10, 11, 12]
})
st.write("This is a DataFrame:")
st.write(df)

##create a line chart
char_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(char_data)


