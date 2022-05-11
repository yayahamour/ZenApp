import streamlit as st
import login
from dotenv import load_dotenv
from pathlib import Path
import os

def main():

    if 'user' in st.session_state:
        st.session_state.user.home()
    else:
        log = login.component()
        if log: st.session_state.user = log
        

if __name__ == "__main__":
    load_dotenv(dotenv_path=Path(".env"))
    main()