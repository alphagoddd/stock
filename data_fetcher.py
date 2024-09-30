from data.historical.historical_data_fetcher import fetch_historical_data
from data.real_time.real_time_data_fetcher import fetch_real_time_data
from data.news.news_data_fetcher import fetch_news_data
from data.economic.economic_data_fetcher import fetch_economic_data

def fetch_all_data(ticker, start_date, end_date):
    print("Fetching historical data...")
    fetch_historical_data(ticker, start_date, end_date, "C:/Users/Bhargav/stock_analysis/data/historical")
    
    print("Fetching real-time data...")
    fetch_real_time_data(ticker, "C:/Users/Bhargav/stock_analysis/data/real_time")
    
    print("Fetching news data...")
    fetch_news_data("stock market", start_date, end_date, "C:/Users/Bhargav/stock_analysis/data/news")
    
    print("Fetching economic data...")
    fetch_economic_data("FRED/GDP", "C:/Users/Bhargav/stock_analysis/data/economic")

if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2023-09-29"
    fetch_all_data(ticker, start_date, end_date)
