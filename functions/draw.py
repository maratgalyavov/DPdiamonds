import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def drawpie(i):
    fig, ax = plt.subplots()
    i.plot.pie()
    st.pyplot(fig)

def drawbar(title, set, df, filter):
    fig, ax = plt.subplots()
    price = []
    plt.title(title)
    for i in set:
        price.append((df[df[filter] == i])["price"].mean())
    plt.bar(["All"]+set,[df["price"].mean()]+price)
    st.pyplot(fig)