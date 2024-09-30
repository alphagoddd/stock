import pandas as pd
import os

def clean_economic_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")

    df = pd.read_csv(file_path)
    df.fillna(method='ffill', inplace=True)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    file_path = "../data/economic/FRED_GDP_data.csv"
    clean_economic_data(file_path)

