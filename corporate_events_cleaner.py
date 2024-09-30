import json
import os

def clean_corporate_events(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")

    with open(file_path, "r") as file:
        events_data = json.load(file)

    cleaned_data = []
    for event in events_data['earnings']:
        cleaned_data.append({
            'date': event['fiscalDateEnding'],
            'type': 'Earnings',
            'earnings': event['reportedEPS']
        })

    output_cleaned_file = file_path.replace('.json', '_cleaned.json')
    with open(output_cleaned_file, 'w') as outfile:
        json.dump(cleaned_data, outfile)

if __name__ == "__main__":
    file_path = "../data/corporate_events/AAPL_events.json"
    clean_corporate_events(file_path)
