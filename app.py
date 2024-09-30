from flask import Flask, render_template, request
import json
import os
import pandas as pd
from config import settings

app = Flask(__name__)

# Load API keys
with open(os.path.join('config', 'api_keys.json')) as f:
    api_keys = json.load(f)

# Load settings
with open(os.path.join('config', 'settings.yaml')) as f:
    config = yaml.safe_load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    ticker = request.form.get('ticker')
    
    # Fetch and analyze the data
    historical_data = pd.read_csv(os.path.join(config['data']['historical_data_path'], f'{ticker}_historical_data.csv'))
    # Perform further analysis here...
    
    return render_template('results.html', data=historical_data.to_html())

if __name__ == "__main__":
    app.run(debug=True)
