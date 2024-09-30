import json
import os

def clean_news_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    
    with open(file_path, "r") as file:
        news_data = json.load(file)

    cleaned_data = []
    for article in news_data['articles']:
        cleaned_data.append({
            'title': article['title'],
            'description': article['description'],
            'source': article['source']['name']
        })

    output_cleaned_file = file_path.replace('.json', '_cleaned.json')
    with open(output_cleaned_file, 'w') as outfile:
        json.dump(cleaned_data, outfile)

if __name__ == "__main__":
    file_path = "../data/news/stock_market_news.json"
    clean_news_data(file_path)
