import unittest
from scripts.recommendation import generate_recommendations

class TestRecommendation(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Close': [150, 152, 153, 155, 154, 158],
            'prediction': [1, 0, 1, 1, 0, 1]  # 1: Buy, 0: Sell
        })

    def test_generate_recommendations(self):
        recommendations = generate_recommendations(self.df)
        self.assertGreater(len(recommendations), 0)
        self.assertIn('Buy', recommendations[0])

if __name__ == '__main__':
    unittest.main()
