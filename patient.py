import streamlit as st
from datetime import date
import requests
import os
from datetime import date
API_URL = os.environ.get("API_URL")

class Patient():
    def __init__(self, username, name, surname):
        self.username = username
        self.name = name
        self.surname = surname
    
    def home(self):
        st.write("Welcome "+ self.name + " " + self.surname)
        calendar = st.date_input('Date', max_value=date.today())
        text = self.get_text(calendar)
        if (calendar == date.today()):
            text_area = st.text_area("Personal Diary " + str(calendar), text, height=200)
            if st.button("Update"):
                self.post_text(text_area)
        else:
            st.write("Personal Diary " + str(calendar))
            st.code(text, language="markdown")

    def get_text(self, date):
        response = requests.get(f"{API_URL}/text?username={self.username}&date={date.strftime('%Y-%m-%d')}")
        
        if response.status_code == 200:
            return response.json()["text"]
        else:
            return "Couldn't fetch the ressource"

    def post_text(self, text):
        text_data = {
            "text": text,
            "user_username": self.username
        }
        response = requests.post(f"{API_URL}/text", json=text_data)

        if response.status_code == 200:
            st.write("Successfully posted / updated the text")
        else:
            st.write("There was an error when trying to post / update your text")
        
        