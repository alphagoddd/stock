import pandas as pd

def calculate_indicators(file_path):
    df = pd.read_csv(file_path)
    
    # Calculate EMA
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    
    # Calculate RSI
    delta = df['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # Calculate VWAP
    df['VWAP'] = (df['Volume'] * (df['High'] + df['Low'] + df['Close']) / 3).cumsum() / df['Volume'].cumsum()
    
    df.dropna(inplace=True)
    
    # Save the calculated data
    df.to_csv(file_path, index=False)
    return df

if __name__ == "__main__":
    file_path = "../data/historical/AAPL_historical_data.csv"
    df = calculate_indicators(file_path)
    print("Indicators calculated and saved.")
