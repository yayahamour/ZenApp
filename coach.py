import streamlit as st
from datetime import date
import hashlib
class Coach():
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def home(self):
        #ajout requete pour completer
        st.write("Welcome "+ self.first_name + " " + self.last_name)
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
                first_name = st.text_input("first_name")
                last_name = st.text_input("last_name")
                #password = st.text_input("User Password",)
                speudo = st.text_input("User username")
                if (st.button("Add")):
                    pass
                #ajout bdd
            elif (action == "Update"):
                list_user = ['user']#request api pour liste utilisateur
                user_select = st.selectbox("User", ["user"])
                if(st.button("Modification")):
                    #ajout pre remplissage en foncion de celui selectionner
                    first_name = st.text_input("first_name")
                    last_name = st.text_input("last_name")
                    #password = st.text_input("User Password",)
                    speudo = st.text_input("User username")
                    if(st.button("Update")):
                        pass
                    #ajout base
                if(st.button("Delete")):
                    pass
                    #suprresion base
                