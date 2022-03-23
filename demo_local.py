import streamlit as st
import json

from main import toApp

st.set_page_config(page_title='Powerplant Production Calculator')
st.title('Powerplant Production Calculator')
st.subheader('Feed me your .json file')

uploaded_file = st.file_uploader('Choose an .json file', type='json')
if uploaded_file:
    toSplit = json.load(uploaded_file)
    response = toApp(toSplit)
    st.json(response)
else:
    response = "Please drag and drop a .json file with the right structure"
    st.write(response)
