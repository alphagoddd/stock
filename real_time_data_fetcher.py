import yfinance as yf
import time
import os

def fetch_real_time_data(ticker, output_dir):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="1m")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    data.to_csv(f"{output_dir}/{ticker}_real_time.csv", mode='a')  # Append new data

if __name__ == "__main__":
    output_directory = "../data/real_time"
    while True:
        fetch_real_time_data("AAPL", output_directory)
        time.sleep(60)  # Fetch every 60 seconds
