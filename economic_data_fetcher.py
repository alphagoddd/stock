import quandl
import os

quandl.ApiConfig.api_key = "33z1DSY4zTPiJm_D_PQY"

def fetch_economic_data(indicator_code, output_dir):
    data = quandl.get(indicator_code)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data.to_csv(f"{output_dir}/{indicator_code}_data.csv")

if __name__ == "__main__":
    output_directory = "../data/economic"
    fetch_economic_data("FRED/GDP", output_directory)  # Fetch GDP data

