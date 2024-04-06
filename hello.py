import streamlit as st
st.title("Welcome to the Oil detection app")
x= st.camera_input("option 1")
btn =st.button("predict")
if btn:
    st.text("Button Clicked!")