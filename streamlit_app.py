import streamlit as st
import requests

API_URL = "https://tourism-agent.onrender.com/ask"

st.set_page_config(page_title="Tourism Assistant", layout="centered")

st.title("🌍 Tourism Multi-Agent Assistant")
st.write("Ask about weather or places to visit in any city!")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json={"message": user_input})

        if response.status_code == 200:
            data = response.json()
            st.success("Here's what I found:")
            st.text_area("Response:", value=data["reply"], height=200)
        else:
            st.error("Something went wrong! API returned an error.")
