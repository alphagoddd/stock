import requests
import json
import os

API_KEY = "53XKO99KLUCZEEK2"

def fetch_corporate_events(ticker, output_dir):
    url = f"https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    events_data = response.json()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f"{output_dir}/{ticker}_events.json", "w") as file:
        json.dump(events_data, file)

if __name__ == "__main__":
    output_directory = "../data/corporate_events"
    fetch_corporate_events("AAPL", output_directory)
