import pandas as pd

def cleanup(df):
    tmp = len(df)
    df.dropna()
    for i in ["carat", "depth", "table", "x", "y", "z"]:
        if df[i].dtypes != "float64":
            df.astype({i:"float64"}).dtypes
    if df["price"].dtypes != "int64":
        df.astype({"price":"int64"}).dtypes
    return df