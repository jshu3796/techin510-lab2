import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Flower Explorer",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title("💐 Flower Explorer")

# Load the dataset
df = pd.read_csv('/mnt/data/IRIS.csv')

# Input filter option for sepal length
sepal_length_slider = st.slider(
    "Sepal Length (mm)",
    min_value=float(df['sepal_length'].min()),
    max_value=float(df['sepal_length'].max()),
    value=float(df['sepal_length'].min())  # Sets the default value to the minimum
)

# Filtering the dataframe based on the slider
df_filtered = df[df['sepal_length'] >= sepal_length_slider]

# Species filter
species_filter = st.selectbox(
    "Species",
    options=df_filtered["species"].unique()
)

# Apply species filter
df_filtered = df_filtered[df_filtered["species"] == species_filter]

st.write(df_filtered)

# Plotting histogram of sepal length
fig = px.histogram(
    df_filtered,
    x="sepal_length",
    title="Sepal Length Distribution"
)
st.plotly_chart(fig)
