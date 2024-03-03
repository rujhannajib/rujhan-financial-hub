import streamlit as st

tickers = []

st.write("Rujhan's Financial Hub")

title = st.text_input('Enter stock ticker')
if title:
    tickers.append(title)

st.write(tickers)