import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "data.csv")

st.title("Dashboard - Laptop Data")



df = pd.read_csv(DATA_PATH)
st.dataframe(df)

brand = st.selectbox("Select the Brand:", df['Brand'].unique())
generation = st.selectbox("Select the Generation:", df['Generation'].unique())

RAM= st.selectbox("Select the RAM:", df['RAM'].unique())
processor = st.selectbox("Select the Processor:", df['Processor'].unique())

price= st.selectbox("Select the Price:", df['Price'].unique())
rating = st.selectbox("Select the Rating:", df['Rating'].unique())

