import streamlit as st
import pandas as pd

st.markdown("# Cleanup logs️")

df1 = pd.read_csv("DiamondsPrices.csv")
tmp = len(df1)
df1.dropna()
fl = True
if len(df1) == tmp:
    st.write("No NaN fields detected")
else:
    st.write("Cleaned up NaN values, dropped {0} rows".format(tmp - len(df)))
for i in ["carat", "depth", "table", "x", "y", "z"]:
    if df1[i].dtypes != "float64":
        st.write("wrong data type in column {0}, must be float64".format(i))
        fl = False
if df1["price"].dtypes != "int64":
    st.write("wrong data type in column price, must be int64")
    fl = False
if fl:
    st.write("all data types are correct")
st.write("cleanup complete")