# main.py
from data_collection import fetch_stock_data
from data_cleaning import clean_data
from data_analysis import calculate_daily_returns
from data_visualization import plot_stock_price

def main():
    # Define stock ticker, start, and end dates
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    
    # Fetch data
    data = fetch_stock_data(ticker, start_date, end_date)
    
    # Clean data
    cleaned_data = clean_data(data)
    
    # Analyze data
    daily_returns = calculate_daily_returns(cleaned_data)
    
    # Visualize data
    plot_stock_price(cleaned_data, ticker)
    
    # Optional: Display or further process the daily_returns
    # print(daily_returns)

if __name__ == "__main__":
    main()
