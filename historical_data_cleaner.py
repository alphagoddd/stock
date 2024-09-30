import pandas as pd
import os

def clean_historical_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    
    df = pd.read_csv(file_path)
    df.fillna(method='ffill', inplace=True)  # Fill missing values
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    file_path = "../data/historical/AAPL_historical_data.csv"
    clean_historical_data(file_path)
