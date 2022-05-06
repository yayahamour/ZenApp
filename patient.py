from faulthandler import disable
from nbformat import write
from sqlalchemy import true
import streamlit as st
from datetime import date

class Patient():
    def __init__(self, login, name, surname):
        self.login = login
        self.name = name
        self.surname = surname
    
    def home(self):
        st.write("Welcome "+ self.name + " " + self.surname)
        calendar = st.date_input('Date', max_value=date.today())
        #test dynamique, remplacer par la requete en fonction du jour :
        text = "" #appel api en fonction du calendar
        if (calendar == date.today()):
            txt = st.text_area("Personal Diary " + str(calendar), text, height=200)
            if st.button("Update"):
                #ajouter modif pour envoie bdd
                st.write("modif")
        else:
            st.write("Personal Diary " + str(calendar))
            st.code(text, language="markdown")
        
        