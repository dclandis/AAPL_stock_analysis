# data_analysis.py
def calculate_daily_returns(data):
    """
    Calculates daily return of stock prices.
    
    Parameters:
    - data: A pandas DataFrame with the stock data.
    
    Returns:
    A pandas Series with daily returns.
    """
    daily_returns = data['Close'].pct_change()
    return daily_returns