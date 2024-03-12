# data_cleaning.py
import pandas as pd

def clean_data(data):
    """
    Cleans the DataFrame data.
    
    Parameters:
    - data: A pandas DataFrame with the stock data.
    
    Returns:
    The cleaned pandas DataFrame.
    """
    # Forward fill missing values
    data.fillna(method='ffill', inplace=True)
    return data