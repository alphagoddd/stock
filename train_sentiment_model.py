import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import os

def train_sentiment_model(news_data_file, output_model_path):
    # Load news data
    df = pd.read_json(news_data_file)
    
    # Preprocess and assign labels (for simplicity, we assume positive/negative classification)
    df['label'] = df['description'].apply(lambda x: 1 if "positive" in x else 0)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(df['description'], df['label'], test_size=0.2, random_state=42)

    # Create a pipeline for vectorization and classification
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # Train the model
    model.fit(X_train, y_train)

    # Save the model
    if not os.path.exists(os.path.dirname(output_model_path)):
        os.makedirs(os.path.dirname(output_model_path))
    joblib.dump(model, output_model_path)

    print(f"Sentiment model saved to {output_model_path}")

if __name__ == "__main__":
    news_data = "../data/news/stock_market_news_cleaned.json"
    model_path = "../models/sentiment_model.pkl"
    train_sentiment_model(news_data, model_path)
