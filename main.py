import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from functions import clean
from functions import draw

st.markdown("# Main project page️")

df = pd.read_csv("DiamondsPrices.csv")
df = clean.cleanup(df)
st.write(
    "The aim of this project is to prove that cut of the diamond has little to no effect on its price, as oppose to clarity and color the most influencial parameter")
print(df["carat"].std())
print(df["carat"].mean())
print(df["carat"].median())
print(df.dtypes)
avg_val = df[(df['carat'] >= 0.5) & (df['carat'] <= 0.6)]
VVS1 = df[df["clarity"] == "VVS1"]
VS1 = df[df["clarity"] == "VS1"]
print(df.info())
print(df.describe())

if st.checkbox('Color'):
    draw.drawpie(df["color"].value_counts())
    names = list(df["color"].unique())
    draw.drawbar("Diamond prices by Тимофей", names, avg_val,"color")

if st.checkbox("Clarity"):
    draw.drawpie(df["clarity"].value_counts())
    names = list(df["clarity"].unique())
    draw.drawbar("Diamond prices by clarity", names, avg_val,"clarity")

if st.checkbox("Cut"):
    draw.drawpie(df["cut"].value_counts())
    names = list(df["cut"].unique())
    draw.drawbar("Diamond prices by clarity", names, avg_val,"cut")
