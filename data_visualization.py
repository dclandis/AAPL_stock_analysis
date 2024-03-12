# data_visualization.py
import matplotlib.pyplot as plt

def plot_stock_price(data, ticker):
    """
    Plots closing stock price of a ticker.
    
    Parameters:
    - data: A pandas DataFrame with the stock data.
    - ticker: Stock symbol of the data being plotted.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label=f'{ticker} Close Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()