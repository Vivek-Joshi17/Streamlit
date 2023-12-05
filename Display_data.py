import streamlit as st

## Load EDA package 
import pandas as pd

st.header("Reading csv file ")
df =pd.read_csv("iris.csv")

#Method 1
st.dataframe(df)

## adding color style from pandas
st.dataframe(df.style.highlight_max(axis=0))

#Method 2:Static table
st.table(df)

# Method 3:using superfunc st.write

st.write(df.head())

# Display Json
st.json({'data':'name'})

#Display Code
mycode ="""
def dayhello():
    print("Hello streamlit")
end
"""
st.code(mycode,language='java')