from faulthandler import disable
from nbformat import write
from sqlalchemy import true
import streamlit as st
from datetime import date

class Patient():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def home(self):

        
        calendar = st.date_input('Date', max_value=date.today())
        #test dynamique, remplacer par la requete en fonction du jour :
        tab = []
        for i in range(0,6):
            tab.append('''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it wa
     the epoch of belief, it was #the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...) 
     '''+ str(i))
        #fin
        if (calendar == date.today()):
            txt = st.text_area("Personal Diary " + str(calendar), tab[calendar.day], height=200)
            if st.button("Update"):
                #ajouter modif pour envoie bdd
                st.write("modif")
        else:
            st.write("Personal Diary " + str(calendar))
            st.code(tab[calendar.day], language="markdown")
        
        