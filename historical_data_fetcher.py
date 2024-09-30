import yfinance as yf
import os

def fetch_historical_data(ticker, start_date, end_date, output_dir):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    data.to_csv(f"{output_dir}/{ticker}_historical_data.csv")
    return data

if __name__ == "__main__":
    output_directory = "../data/historical"
    fetch_historical_data("AAPL", "2020-01-01", "2023-09-29", output_directory)
