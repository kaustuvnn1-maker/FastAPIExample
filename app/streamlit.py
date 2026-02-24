import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("FastAPI + Streamlit Integration")

menu = st.sidebar.selectbox("Choose Action", ["Get All Posts", "Create Post","get Post ID"])

if menu == "Get All Posts":
    if st.button("Fetch Posts"):
        response = requests.get(f"{BASE_URL}/posts")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Failed to fetch posts")

elif menu == "Create Post":
    title = st.text_input("Title")
    content = st.text_area("Content")

    if st.button("Submit"):
        payload = {
            "title": title,
            "content": content
        }
        response = requests.post(f"{BASE_URL}/posts", json=payload)

        if response.status_code == 201:
            st.success("Post Created Successfully")
        else:
            st.error(response.text)
elif menu == "get Post ID":
    id = st.text_input("ID")
    id_int = int(id)
    response = requests.get(f"{BASE_URL}/posts/{id_int}")
    if response.status_code == 200:
            st.json(response.json())
    else:
            st.error("ID does not exist")
