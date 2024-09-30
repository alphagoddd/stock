import requests
import json
import os

API_KEY = "7211a81d425945a388ef8dbc29b75c56"

def fetch_news_data(query, from_date, to_date, output_dir):
    url = (f"https://newsapi.org/v2/everything?q={query}"
           f"&from={from_date}&to={to_date}&apiKey={API_KEY}")
    response = requests.get(url)
    news_data = response.json()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(f"{output_dir}/{query}_news.json", "w") as file:
        json.dump(news_data, file)

if __name__ == "__main__":
    output_directory = "../data/news"
    fetch_news_data("stock market", "2023-09-28", "2023-09-29", output_directory)
