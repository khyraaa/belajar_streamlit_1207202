import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.header("_Streamlit_is :blue[cool] :sunglasses:")

st.subheader("_Streamlit_is :blue[cool] :sunglasses:")

st.markdown("*Streamlit* is  **really** ***cool***.")

st.metric(label="Temperature", value="70")

import panda as pd
import numpy as np

chart_data = pdd.DataFraame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

if st.button("Say hello");
    st.write("Why hello tehere")

