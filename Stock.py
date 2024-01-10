import streamlit as st
import yfinance as yf
import datetime

# Set the page title
st.title("Stock Market Data Explorer")

# Sidebar for user input
st.sidebar.header("User Input")

# Select stock symbol
symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL").upper()

# Select date range
start_date = st.sidebar.date_input("Start Date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

# Fetch stock data using Yahoo Finance
@st.cache  # Cache the function to improve performance
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

stock_data = get_stock_data(symbol, start_date, end_date)

# Display stock data
st.header(f"Stock Data for {symbol}")
st.write(stock_data)

# Plot stock closing price
st.header(f"Closing Price Chart for {symbol}")
st.line_chart(stock_data['Close'])

# Display additional information
st.header("Additional Information")
st.write(f"Number of Trading Days: {len(stock_data)}")
st.write(f"Data Range: {start_date} to {end_date}")
st.write(f"Max Closing Price: {stock_data['Close'].max()}")
st.write(f"Min Closing Price: {stock_data['Close'].min()}")
st.write(f"Average Closing Price: {stock_data['Close'].mean()}")
