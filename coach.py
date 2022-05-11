from turtle import onclick
import streamlit as st
from datetime import date
import os
import requests
API_URL = os.environ.get("API_URL")

class Coach():
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def home(self):
        st.write("Welcome "+ self.first_name + " " + self.last_name)
        option = st.radio("Option", ["Graph", "Management"])

        if(option == "Graph"):
            user_list = self.get_users(keep_admins=False)
            usernames = [user["username"] for user in user_list]
            user = st.selectbox("User", usernames)

            research_type =st.radio("Time", ["to day", "last week", "last month", "last year", "custom"])
            if (research_type == "custom"):
                start = st.date_input('Start', max_value=date.today())
                end = st.date_input('End', max_value=date.today(), min_value=start)
                
        if(option == "Management"):
            action = st.radio("Action", ["Add", "Update"])
            if (action == "Add"):
                first_name = st.text_input("first_name")
                last_name = st.text_input("last_name")
                username = st.text_input("User username")

                if (st.button("Add")):
                    st.write(self.create_user(first_name, last_name, username))

            elif (action == "Update"):
                user_list = self.get_users(keep_admins=True)
                usernames = [user["username"] for user in user_list]
                selected_user = st.selectbox("User", usernames)

                selected_user = [user for user in user_list if user["username"] == selected_user][0]

                selected_user["first_name"] = st.text_input("first_name", selected_user["first_name"])
                selected_user["last_name"] = st.text_input("last_name", selected_user["last_name"])

                if(st.button("Update")):
                    st.write(self.update_user(selected_user))

                if(st.button("Delete")):
                    st.write(self.delete_user(selected_user["username"]))
                


    def get_users(self, keep_admins):
        url = f"{API_URL}/userlist?admins={keep_admins}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            st.error("Can't fetch the user list at the moment")

    def create_user(self, first_name, last_name, username):
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

    def update_user(self, infos):
        API_URL = os.environ.get("API_URL")

        response = requests.put(f"{API_URL}/user", json=infos)
        if response.status_code == 200:
            return f"Successfully updated user {infos['username']}"
        else:
            return "Can't update this user"

    def delete_user(self, username):
        API_URL = os.environ.get("API_URL")
        response = requests.delete(f"{API_URL}/user?username={username}")

        if response.status_code == 200:
            return f"Successfully deleted user {username}"
        else:
            return "Can't delete this user"