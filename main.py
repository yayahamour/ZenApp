import streamlit as st
from login import Login
from dotenv import load_dotenv
from pathlib import Path

def main():
    dotenv_path = Path("var.env")
    load_dotenv(dotenv_path=dotenv_path)
    log = Login()     
    log.login()
    
main()