import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as plot

st.set_page_config(
    page_title="flower explorer",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state = "auto",
    menu_items = None
)

st.title("💐flower explorer")

df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')

#input filter option
bill_length_slider = st.slider(
    "Bill Length(mm)"
    min(df[bill_length_mm]),
    max(df[bill_length_mm]),
)

df = df[df['bill_length_mm']>bill_length_slider]

species_filter = st.selectbox(
    "species", 
    df["species"].unique()
    index=None)

islands_filter = st.selectbox("Island", df["Island"].unique())


#filter data
if species_filter:
    df = df[df["species"] == species_filter]
df = df[df["island"].isin(islands_filter)]
st.write(df)


fig = px.historgram(
    df,
    x="bill_length_mm"
)
st.plot_chart(fig)