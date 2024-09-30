import pandas as pd
import os

def clean_real_time_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")

    df = pd.read_csv(file_path)
    df.fillna(method='ffill', inplace=True)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    file_path = "../data/real_time/AAPL_real_time.csv"
    clean_real_time_data(file_path)
