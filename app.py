import streamlit as st
import pandas as pd
import requests

API_KEY = "QByDSMG5IDJ4gsSb0gAq7G12UzvKtag2"

st.title("Financial Modeling Prep Test")

# Load tickers
tickers = pd.read_csv("tickers.csv")

st.write(f"Tickers Loaded: {len(tickers)}")

# Use first ticker as a test
ticker = tickers.iloc[0]["Ticker"]

url = (
    f"https://financialmodelingprep.com/api/v3/profile/"
    f"{ticker}?apikey={API_KEY}"
)

response = requests.get(url)

data = response.json()

st.subheader("API Response")

st.write(data)
