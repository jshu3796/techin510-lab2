import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="flower explorer",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state = "auto",
    menu_items = None
)

st.title("💐flower explorer")

df = pd.read_csv('IRIS.csv')
st.write(df)