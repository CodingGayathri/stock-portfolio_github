import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define your stock portfolio (stock symbol, number of shares, buy price)
portfolio = {
    'AAPL': {'shares': 10, 'buy_price': 150},
    'GOOGL': {'shares': 5, 'buy_price': 2000},
    'MSFT': {'shares': 8, 'buy_price': 250},
}

# Function to fetch stock data and return current price
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period='1d')
    return stock_data['Close'][0]

# Function to calculate total portfolio value
def calculate_portfolio_value(portfolio):
    total_value = 0
    for stock, data in portfolio.items():
        current_price = get_stock_data(stock)
        total_value += current_price * data['shares']
    return total_value

# Function to display stock gains/losses
def display_gains(portfolio):
    for stock, data in portfolio.items():
        current_price = get_stock_data(stock)
        gain = (current_price - data['buy_price']) * data['shares']
        print(f"{stock}: Current Price = ${current_price:.2f}, Gain/Loss = ${gain:.2f}")

# Visualize portfolio stock price trends
def visualize_stocks(portfolio):
    stock_symbols = " ".join(portfolio.keys())
    stock_data = yf.download(stock_symbols, period="1mo")['Close']
    
    stock_data.plot(title="Stock Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.show()

# Display portfolio value and gains/losses
def display_portfolio_summary(portfolio):
    print(f"Total Portfolio Value: ${calculate_portfolio_value(portfolio):.2f}")
    display_gains(portfolio)

# Main function
def main():
    display_portfolio_summary(portfolio)
    visualize_stocks(portfolio)

if __name__ == "__main__":
    main()