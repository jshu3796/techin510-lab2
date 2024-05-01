import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
np.random.seed(42)

import plotly.express as px
print("Plotly is installed correctly!")

st.set_page_config(
    page_title="Flower Explorer",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title("💐 Flower Explorer")
st.markdown("This dataset includes measurements of the sepal length and width, and petal length and width of 150 iris flowers from three different species. It's commonly used for classification and visualization tasks.")

# Load the dataset
df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')

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


np.random.seed(42)  # For reproducible results
df['latitude'] = np.random.uniform(-90, 90, size=len(df))
df['longitude'] = np.random.uniform(-180, 180, size=len(df))
fig2 = px.scatter_geo(df,
                     lat='latitude',
                     lon='longitude',
                     color='species',
                     title="Geographical Distribution of Iris Species")

st.plotly_chart(fig2)
