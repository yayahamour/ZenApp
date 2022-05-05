import streamlit as st
from patient import Patient
from coach import Coach

class Login():
       
    def patient_page(self, login, password):
        if(login == "yaya"):
            page = Patient(0, "yaya")
            page.home()
        elif(login == "admin"):
            page = Coach()
            page.home()
    
    
    
    def login(self):
        login = st.sidebar.text_input("Login")
        password = st.sidebar.text_input("Password")
        st.sidebar.button("Login", on_click=self.patient_page(login, password))
            
        
        
        
    