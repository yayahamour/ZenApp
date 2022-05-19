import streamlit as st
from datetime import date
import requests
import os
from datetime import date
from api_functions import get_text, post_text


class Patient():
    def __init__(self, username, name, surname):
        self.username = username
        self.name = name
        self.surname = surname
    
    def home(self):
        st.write("Welcome "+ self.name + " " + self.surname)
        calendar = st.date_input('Date', max_value=date.today())
        text = get_text(self.username, calendar)["text"]
        if (calendar == date.today()):
            text_area = st.text_area("Personal Diary " + str(calendar), text, height=200)
            if st.button("Update"):
                post_text(self.username, text_area)
        else:
            st.write("Personal Diary " + str(calendar))
            st.code(text, language="markdown")
        
        