import streamlit as st
sal=st.number_input("Enter your salary")
credit=st.number_input("Enter your credit score")
if sal>=50000 and credit>=500:
     st.write('congratulations')
st.balloons()