import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def train_stock_model(historical_data_file, output_model_path, output_scaler_path):
    # Load historical stock data
    df = pd.read_csv(historical_data_file)
    
    # Features: we take price, volume, and simple moving averages
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()

    df.dropna(inplace=True)

    X = df[['Close', 'Volume', 'SMA_50', 'SMA_200']]
    y = (df['Close'].shift(-1) > df['Close']).astype(int)  # Predict if stock will go up (1) or down (0)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Save the model and scaler
    if not os.path.exists(os.path.dirname(output_model_path)):
        os.makedirs(os.path.dirname(output_model_path))
    joblib.dump(model, output_model_path)
    joblib.dump(scaler, output_scaler_path)

    print(f"Stock model saved to {output_model_path}")
    print(f"Scaler saved to {output_scaler_path}")

if __name__ == "__main__":
    historical_data = "../data/historical/AAPL_historical_data.csv"
    model_path = "../models/stock_model.pkl"
    scaler_path = "../models/scaler.pkl"
    train_stock_model(historical_data, model_path, scaler_path)
