import streamlit as st
from datetime import date, timedelta
from api_functions import get_text, get_emotions, list_users, create_user, update_user, delete_user
import pandas as pd
import matplotlib.pyplot as plt
class Coach():
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name


    def graph(self, dict):
        df = pd.DataFrame.from_dict(dict)
        sizes = df.groupby('emotion').count().reset_index()["text"]
        labels = df['emotion'].unique()      
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels,autopct='%1.1f%%', startangle=15)
        ax.axis('equal')
        ax.set_facecolor('black')
        st.pyplot(fig)
            
            
            
    def home(self):
        st.write("Welcome "+ self.first_name + " " + self.last_name)
        option = st.radio("Option", ["Informations", "Management"])

        if(option == "Informations"):
            user_list = list_users(keep_admins=False)
            usernames = ["all"] + [user["username"] for user in user_list]
            user = st.selectbox("User", usernames)
            if (user != "all"):
                text_date = st.date_input('Text date', max_value=date.today())
                response = get_text(user, text_date)
                st.code(response["text"], language="markdown")
                if (response.get("emotion") != None):
                    st.write(response["emotion"])
            choix =  ["last week", "last month", "last year", "custom"]
            research_type =st.radio("Time", choix)
            if (research_type == "custom"):
                start = st.date_input('Start', max_value=date.today())
                end = st.date_input('End', max_value=date.today(), min_value=start)
            elif(research_type == "last week"):
                end = date.today()
                start = end - timedelta(days=7)
            elif(research_type == "last month"):
                end = date.today()
                start = end - timedelta(weeks=4)
            elif(research_type == "last year"):
                end = date.today()
                start = end - timedelta(weeks=52)
            if (user == "all"):
                response = get_emotions(start = start, end=end)
            else:
                response = get_emotions(start = start, end=end, username= user)
            if (type(response) is list):
                self.graph(response)
                
        if(option == "Management"):
            action = st.radio("Action", ["Add", "Update"])
            if (action == "Add"):
                first_name = st.text_input("first_name")
                last_name = st.text_input("last_name")
                username = st.text_input("User username")

                if (st.button("Add")):
                    st.write(create_user(first_name, last_name, username))

            elif (action == "Update"):
                user_list = list_users(keep_admins=True)
                usernames = [user["username"] for user in user_list]
                selected_user = st.selectbox("User", usernames)

                selected_user = [user for user in user_list if user["username"] == selected_user][0]

                selected_user["first_name"] = st.text_input("first_name", selected_user["first_name"])
                selected_user["last_name"] = st.text_input("last_name", selected_user["last_name"])

                if(st.button("Update")):
                    st.write(update_user(selected_user))

                if(st.button("Delete")):
                    st.write(delete_user(selected_user["username"]))
