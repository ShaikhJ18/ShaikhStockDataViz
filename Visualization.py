import streamlit as st
import humanize;
import yfinance as yf
import pandas as pd;
import requests
import matplotlib.pyplot as plt

st.title("Welcome to Shaikh Stock Price Data Visualization")

ticker = st.text_input("Enter stock ticker:")


if ticker:
    data = yf.Ticker(ticker).history(period="max")
    info  = yf.Ticker(ticker).info
    officers = info['companyOfficers']
    ceo = officers[0]
    st.header(f"{info['longName']} ({info['industry']})")
    st.image(f"https://img.logo.dev/ticker/{ticker}?token=pk_dpyQ8FKpR9-ixdnpNhAOkg&retina=true")
    st.header(f"Market Cap of ${humanize.intword(info['marketCap'])} ({info['currency']})")
    st.header(f"CEO is {ceo['name']}");
    st.header("Company Information")
    st.text(f"{info['longBusinessSummary']}")
    st.header("Contact Information")
    st.text(f"{info['address1']}, {info['city']}, {info['state']}, {info['zip']}, {info['country']}")
    st.text(f"Phone Number: {info['phone']}")
    st.markdown(f"Website: {info['website']}")
    st.write(data)
    st.write()
    
    date_range = st.date_input("Select date range", [])
    if date_range:
        filtered_data = data[date_range[0]:date_range[1]]
        st.line_chart(filtered_data['Close'])
        
    fig, ax = plt.subplots()
    data['Close'].plot(ax=ax)
    st.pyplot(fig)
