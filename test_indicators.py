import unittest
import pandas as pd
from scripts.indicator_calculator import calculate_indicators

class TestIndicatorCalculator(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Close': [150, 152, 153, 155, 154, 158],
            'Volume': [1000, 1100, 1050, 1200, 1150, 1300]
        })

    def test_calculate_indicators(self):
        result = calculate_indicators(self.df)
        self.assertIn('EMA_20', result.columns)
        self.assertIn('RSI', result.columns)

if __name__ == '__main__':
    unittest.main()
