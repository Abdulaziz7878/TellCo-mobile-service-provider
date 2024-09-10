import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(page_title="Sales Dashboard",
                    page_icon=":bar_chart:",
                    layout="wide"
                    )
st.title("TellCo analysis")
data = pd.read_csv(r"C:\Users\Abdulaziz\Desktop\10 Academy\TellCo mobile service provider\notebooks\cleand-data.csv")
st.write(data)

top_10_handsets = data['Handset Type'].value_counts().head(10)
st.header("top 10 handsets")
st.write(top_10_handsets)

st.header("top 3 handsets Manufacturer")
top_3_handsets = data['Handset Manufacturer'].value_counts().head(3)
st.write(top_3_handsets)

top_3_manufacturers = data['Handset Manufacturer'].value_counts().head(3).index
# For each of the top 3 manufacturers, get the top 5 handsets
for manufacturer in top_3_manufacturers:
    st.write(f"Top 5 handsets manufactured by {manufacturer}:")
    top_5_handsets = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
    st.write(top_5_handsets)