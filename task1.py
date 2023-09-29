import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector

st.set_page_config(page_title='E-commerce Site', page_icon=':dna:')
st.markdown(f'<h1 style="text-align: center;"> E-commerce Site</h1>', unsafe_allow_html=True)

SELECT = option_menu(
    menu_title=None,
    options=["Register", "Login"],
    icons=["house", "toggles"],
    default_index=0,
    orientation="horizontal")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()


if SELECT == "Register":

    st.header("Registration")
    First_name = st.text_input("First Name:  ")
    Last_name = st.text_input("Last Name:  ")
    Phone_num = st.text_input("Phone Number:  ")
    email = st.text_input("Email ID:  ")
    Password = st.text_input("Password: ")
    v = st.button("Submit")
    if v:
        try:
            cursor.execute("use tom")
            cursor.execute(f"INSERT  ignore INTO registeration (first_name, last_name, email, phone_num, password) VALUES ('{First_name}', '{Last_name}', '{email}', '{Phone_num}', '{Password}')")
            conn.commit()
            st.success("Successfully Registeration Completed")
        except:
            st.error("Error in the Inputs ")


if SELECT == "Login":
    st.header("Login")
    User_Name = st.text_input("User Name:", placeholder = "Enter Email ID")
    password = st.text_input("Password:")
    l = st.button("Login")
    if l:
        cursor.execute("use tom")
        query = f"select password from registeration where email = '{User_Name}'"
        password_check = pd.read_sql(query, conn)
        column_values = password_check['password'].values  # Extract values from 'Column1'

        # Compare DataFrame values to the global variable
        for value in column_values:
            if value == password:
                st.success("success")
                break
        else:
            st.error("error")











