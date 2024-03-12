# data_collection.py
import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data for a ticker from start_date to end_date.
    
    Parameters:
    - ticker: Stock symbol to fetch.
    - start_date: Start date in 'YYYY-MM-DD' format.
    - end_date: End date in 'YYYY-MM-DD' format.
    
    Returns:
    A pandas DataFrame with historical stock data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data
