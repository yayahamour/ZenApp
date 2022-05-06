import streamlit as st
from datetime import date
import hashlib
class Coach():
    def __init__(self, login, name, surname):
        self.login = login
        self.name = name
        self.surname = surname

    def home(self):
        #ajout requete pour completer
        st.write("Welcome "+ self.name + " " + self.surname)
        option = st.radio("Option", ["Graph", "Management"])
        if(option == "Graph"):
            user = st.selectbox("User", ["all", "user1", "user2"])
            type_recherche =st.radio("Time", ["to day", "last week", "last month", "last year", "personalise"])
            
            
            if (type_recherche == "personalise"):
                start = st.date_input('Start', max_value=date.today())
                end = st.date_input('End', max_value=date.today(), min_value=start)
        if(option == "Management"):
            action = st.radio("Action", ["Add", "Update"])
            if (action == "Add"):
                name = st.text_input("Name")
                surname = st.text_input("Surname")
                #password = st.text_input("User Password",)
                speudo = st.text_input("User Login")
                if (st.button("Add")):
                    pass
                #ajout bdd
            elif (action == "Update"):
                list_user = ['user']#request api pour liste utilisateur
                user_select = st.selectbox("User", ["user"])
                if(st.button("Modification")):
                    #ajout pre remplissage en foncion de celui selectionner
                    name = st.text_input("Name")
                    surname = st.text_input("Surname")
                    #password = st.text_input("User Password",)
                    speudo = st.text_input("User Login")
                    if(st.button("Update")):
                        pass
                    #ajout base
                if(st.button("Delete")):
                    pass
                    #suprresion base
                