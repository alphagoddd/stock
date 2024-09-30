from data.historical.historical_data_cleaner import clean_historical_data
from data.real_time.real_time_data_cleaner import clean_real_time_data
from data.news.news_data_cleaner import clean_news_data
from data.economic.economic_data_cleaner import clean_economic_data

def preprocess_all_data():
    print("Cleaning historical data...")
    clean_historical_data("../data/historical/AAPL_historical_data.csv")
    
    print("Cleaning real-time data...")
    clean_real_time_data("../data/real_time/AAPL_real_time.csv")
    
    print("Cleaning news data...")
    clean_news_data("../data/news/stock_market_news.json")
    
    print("Cleaning economic data...")
    clean_economic_data("../data/economic/FRED_GDP_data.csv")

if __name__ == "__main__":
    preprocess_all_data()
