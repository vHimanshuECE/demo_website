import streamlit as st
import pandas as pd

# st.title("Welcome to ElectraNotes")
# st.header("my name is Himanshu")
# st.subheader
# st.markdown
# st.code

name = st.text_input("Enter your name: ")
DOB = st.text_input("Enter your D.O.B: ")
age = st.text_input("Enter your age: ")
addr = st.text_area("Enter your address: ")
branch = st.selectbox("Enter your Branch: 1 for ECE, 2 for CSE and 3 for EEE",(1,2,3))

button = st.button("submit")
if button:
    st.markdown(f'''
                Name: {name}
                DOB: {DOB}
                Age: {age}
                Address: {addr}
                Branch: {branch}''')

