from InputLoader import load_users
import streamlit as st
import pandas as pd


class App:

    def __init__(self):
        self.users = {}

    def run(self):
        st.title("User Data")
        users = load_users()
        df = pd.DataFrame(users)
        st.table(df)

