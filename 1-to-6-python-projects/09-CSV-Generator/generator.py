import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]  

   
    if file_extension == "csv":
        df = pd.read_csv(uploaded_file, encoding="utf-8")  
    elif file_extension == "xlsx":
        df = pd.read_excel(uploaded_file, engine="openpyxl") 

        st.subheader("Data Preview")  
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select colum to filter by:", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select value", unique_values)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

        st.subheader("Plot Data")
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select y_axis column", columns)

        if st.button("Generate plot"):
          st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")