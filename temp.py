from tranformers import pipeline
import streamlit as st
pipe = pipeline('text-classification')

st.title("prediction")
txt_input = st.text_input("Enter the string")
if st.button("analysis"):
    if txt_input:
       output = pipe(txt_input)

       st.write("prediction",output)