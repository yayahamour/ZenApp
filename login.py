from lib2to3.pytree import Base
import os
import streamlit as st
from patient import Patient
from coach import Coach
import requests
API_URL = os.environ.get("API_URL")
       
def handle_api(username):
    
    url = f"{API_URL}/user?username={username}"
    response = requests.get(url)
    if response.status_code != 200:
        st.error("This user does not exist or can't be fetched at the moment")
        return

    
    data = response.json()
    if data["is_admin"]:
        user = Coach(data["username"], data["first_name"], data["last_name"])
    else:
        user = Patient(data["username"], data["first_name"], data["last_name"])

    return user


def component():
    login = st.sidebar.text_input("Login")
    if st.sidebar.button("Login") & (login != ""):
        return handle_api(login)
            
        
        
        
    