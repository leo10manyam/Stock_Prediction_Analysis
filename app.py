import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf
import streamlit as st
from keras.model import load_model


# Load the model
model = load_model('keras_model.h5')  # Make sure the file is in the same directory
start = '2010-01-01'
end = '2024-10-10'

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter the stock Ticker', 'AAPL')
df = data.DataReader(user_input, 'yahoo', start, end)

st.subheader('Data from 2010 - 2024')
st.write(df.describe())

