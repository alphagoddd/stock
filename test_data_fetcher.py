import unittest
from scripts.data_fetcher import fetch_historical_data, fetch_news_data

class TestDataFetcher(unittest.TestCase):

    def test_fetch_historical_data(self):
        result = fetch_historical_data("AAPL")
        self.assertIsNotNone(result)
        self.assertIn('Close', result.columns)

    def test_fetch_news_data(self):
        result = fetch_news_data("AAPL")
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
