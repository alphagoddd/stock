import pandas as pd
import joblib

def generate_recommendation(stock_data_file, sentiment_file, model_file, scaler_file):
    # Load stock data, sentiment analysis, and stock model
    stock_df = pd.read_csv(stock_data_file)
    sentiment_df = pd.read_json(sentiment_file)
    stock_model = joblib.load(model_file)
    scaler = joblib.load(scaler_file)

    # Filter based on positive sentiment
    positive_news = sentiment_df[sentiment_df['sentiment'] == 1]
    
    # Prepare stock data for prediction
    X = stock_df[['Close', 'Volume', 'SMA_50', 'SMA_200']]
    X_scaled = scaler.transform(X)
    
    # Generate predictions (1: Buy, 0: Sell)
    predictions = stock_model.predict(X_scaled)
    
    recommendations = []
    for i, pred in enumerate(predictions):
        if pred == 1:
            recommendations.append(f"BUY {stock_df.iloc[i]['Ticker']} at price {stock_df.iloc[i]['Close']}")
        else:
            recommendations.append(f"SELL {stock_df.iloc[i]['Ticker']} at price {stock_df.iloc[i]['Close']}")
    
    return recommendations

if __name__ == "__main__":
    stock_data_file = "../data/historical/AAPL_historical_data.csv"
    sentiment_file = "../data/news/stock_market_news_sentiment.json"
    model_file = "../models/stock_model.pkl"
    scaler_file = "../models/scaler.pkl"
    
    recommendations = generate_recommendation(stock_data_file, sentiment_file, model_file, scaler_file)
    print("\n".join(recommendations))
