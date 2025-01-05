import streamlit as st
import yfinance as yf
import datetime

# Page configuration
st.set_page_config(
    page_title="Stock Market Data Explorer",
    page_icon="📈",
    layout="wide"
)

# Page title and description
st.title("📈 Stock Market Data Explorer")
st.markdown("""
    Explore historical stock market data with ease!  
    - View detailed stock performance.
    - Analyze trends with interactive charts.
    - Fetch data quickly and efficiently.  
    """)

# Sidebar configuration
st.sidebar.header("User Input")
st.sidebar.markdown("Customize your data selection below:")

# Select stock symbol
symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL").upper()

# Select date range
start_date = st.sidebar.date_input("Start Date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

# Error handling for date range
if start_date > end_date:
    st.sidebar.error("Start date must be earlier than end date!")

# Fetch stock data using Yahoo Finance
@st.cache_data  # Use Streamlit's caching for faster performance
def get_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

stock_data = get_stock_data(symbol, start_date, end_date)

# Display stock data
if stock_data is not None and not stock_data.empty:
    st.header(f"📊 Stock Data for **{symbol}**")
    st.write(f"Showing data from **{start_date}** to **{end_date}**")
    st.dataframe(stock_data.style.format("{:.2f}"))

    # Display stock closing price chart
    st.header(f"📉 Closing Price Chart for **{symbol}**")
    st.line_chart(stock_data['Close'])

    # Add additional metrics
    st.header("📌 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Max Closing Price", f"${stock_data['Close'].max():.2f}")
    col2.metric("Min Closing Price", f"${stock_data['Close'].min():.2f}")
    col3.metric("Average Closing Price", f"${stock_data['Close'].mean():.2f}")
    col4.metric("Trading Days", len(stock_data))

    # Advanced charts (Volume and Moving Average)
    st.header("📈 Advanced Charts")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Volume Traded")
        st.bar_chart(stock_data['Volume'])

    with col2:
        st.subheader("Moving Average (50 Days)")
        stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
        st.line_chart(stock_data[['Close', '50_MA']])

else:
    st.warning("No data found! Please adjust your input and try again.")
