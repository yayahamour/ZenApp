import os
import streamlit as st
import requests

API_URL = os.environ.get("API_URL")

# Text Functions
def get_text(username, date):
    API_URL = os.environ.get("API_URL")
    response = requests.get(f"{API_URL}/text?username={username}&date={date.strftime('%Y-%m-%d')}")
    
    if response.status_code == 200:
        return response.json()
    else:
        return "Couldn't fetch the ressource"

def post_text(username, text):
    API_URL = os.environ.get("API_URL")
    text_data = {
        "text": text,
        "user_username": username
    }
    response = requests.post(f"{API_URL}/text", json=text_data)

    if response.status_code == 200:
        st.write("Successfully posted / updated the text")
    else:
        st.write("There was an error when trying to post / update your text")


# User functions
def list_users(keep_admins):
    API_URL = os.environ.get("API_URL")
    url = f"{API_URL}/userlist?admins={keep_admins}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error("Can't fetch the user list at the moment")

def create_user(first_name, last_name, username):
    API_URL = os.environ.get("API_URL")
    infos = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username
    }
    response = requests.post(f"{API_URL}/user", json=infos)
    if response.status_code == 200:
        return f"Successfully created {infos['username']}"
    else:
        return "Can't create this user"

def update_user(infos):
    API_URL = os.environ.get("API_URL")
    response = requests.put(f"{API_URL}/user", json=infos)
    if response.status_code == 200:
        return f"Successfully updated user {infos['username']}"
    else:
        return "Can't update this user"

def delete_user(username):
    API_URL = os.environ.get("API_URL")
    response = requests.delete(f"{API_URL}/user?username={username}")

    if response.status_code == 200:
        return f"Successfully deleted user {username}"
    else:
        return "Can't delete this user"
    
def get_emotions(start, end, username = None):
    API_URL = os.environ.get("API_URL")
    url = f"{API_URL}/emotions?start_date={start.strftime('%Y-%m-%d')}"
    if (end != None):
        url += f"&end_date={end.strftime('%Y-%m-%d')}"
    if (username != None):
        url += f"&username={username}"
    print(url)
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Can't fetch the emotion list at the moment")