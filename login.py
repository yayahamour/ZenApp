import os
import streamlit as st
from patient import Patient
from coach import Coach

class Login():
       
    def patient_page(self, login):
        #debut
        is_admin, name, surname = None, "yanis", "ham"#a changer avec l'api
        if(login == 'yanis'):
            is_admin = False
        elif(login == 'admin'):
            is_admin = True
        #fin
        if(is_admin == False):
            page = Patient(login, name, surname)
            page.home()
        elif(is_admin == True):
            page = Coach(login, name, surname)
            page.home()
    
    
    
    def login(self):
        login = st.sidebar.text_input("Login")
        #password = st.sidebar.text_input("Password")
        st.sidebar.button("Login", on_click=self.patient_page(login))
            
        
        
        
    