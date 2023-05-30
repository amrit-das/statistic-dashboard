import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # data web app development
import pandasai as pdai  # Pandas ai to get data frm query

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

dataset_url = "telecom-churn-data-dummy.csv"

st.set_page_config(
    page_title="Data Dashboard",
    page_icon=":bar-chart:",
    layout="wide",
)

# dashboard title
st.markdown(
    "<h1 style='text-align: center; color: black;'>Data Dashboard</h1>",
    unsafe_allow_html=True,
)

st.text(" ")


@st.cache_data
def get_data(file) -> pd.DataFrame:
    return pd.read_csv(file)


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "<h2 style='text-align: center; color: grey;'>Add Rules/Initialization Here</h2>",
            unsafe_allow_html=True,
        )
    with col2:
        uploaded_file = st.file_uploader("Upload your data file")
        c1, c2, c3, c4, c5 = st.columns(5)
        with c2:
            btn_load = st.button("Load Uploaded")
        with c4:
            btn_dummy = st.button("Load Dummy")

if btn_load:
    if uploaded_file is not None:
        dataframe = get_data(uploaded_file)
        st.header("Loaded Data:")
        st.dataframe(dataframe)
    else:
        raise FileNotFoundError("No Data Loaded, please use dummy data instead")

if btn_dummy:
    dataframe = get_data(dataset_url)
    st.header("Loaded Data:")
    st.dataframe(dataframe)
