# 📈 Stock Market Data Explorer

The **Stock Market Data Explorer** is a Streamlit-based web application that allows users to interactively explore historical stock market data. It leverages the Yahoo Finance API for data retrieval and provides visual insights through dynamic charts and key metrics.

---

## 🚀 Features

- **Real-Time Data Retrieval**: Fetch historical stock data from Yahoo Finance.
- **Dynamic Charts**:
  - Closing Price Trends
  - Volume Traded
  - 50-Day Moving Average
- **Key Metrics**:
  - Max, Min, and Average Closing Prices
  - Total Trading Days
- **Interactive UI**:
  - Input stock symbols and date ranges via the sidebar.
  - Instant updates based on user inputs.
- **Performance Optimization**: Cached data for faster load times.

---

## 📂 Project Structure

```plaintext
Stock/
├── README.md            # Documentation
├── Stock.py             # Main Streamlit application script
```

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Data Source**: Yahoo Finance (via `yfinance` library)
- **Visualization**: Streamlit's built-in charting tools

---

## 🎯 How to Run

### Prerequisites

- Python 3.7 or higher installed.
- Required Python libraries: `streamlit`, `yfinance`.

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Stock-Market-Data-Explorer.git
   cd Stock-Market-Data-Explorer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run Stock.py
   ```

---

### 1. Interactive Sidebar
- Customize stock symbol and date range inputs.

### 2. Key Metrics
- View maximum, minimum, and average prices along with total trading days.

### 3. Dynamic Charts
- Analyze trends with interactive charts for closing prices, volume traded, and moving averages.

---

## 🤝 Contribution

Contributions are welcome! Feel free to:
- Fork the repository.
- Create feature branches.
- Submit pull requests with detailed explanations.

---
