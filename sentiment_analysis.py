import joblib
import pandas as pd

def run_sentiment_analysis(news_data_file, model_file):
    # Load news data and sentiment model
    df = pd.read_json(news_data_file)
    sentiment_model = joblib.load(model_file)

    # Predict sentiment for each article
    df['sentiment'] = sentiment_model.predict(df['description'])
    
    # Positive sentiment articles
    positive_news = df[df['sentiment'] == 1]
    
    # Save sentiment results
    df.to_json(news_data_file.replace('.json', '_sentiment.json'), orient='records')

    print(f"Sentiment analysis completed. Positive articles: {len(positive_news)}")
    return df

if __name__ == "__main__":
    news_data_file = "../data/news/stock_market_news_cleaned.json"
    model_file = "../models/sentiment_model.pkl"
    run_sentiment_analysis(news_data_file, model_file)
