import streamlit as st
from login import Login

def main():
    log = Login()     
    log.login()
    
main()