import unittest
from vertex_trading_bot.data.data_fetcher import DataFetcher
from vertex_trading_bot.config import settings


class TestDataFetcher(unittest.TestCase):
    def setUp(self):
        self.data_fetcher = DataFetcher()

    def test_fetch_historical_data(self):
        data = self.data_fetcher.fetch_historical_data()
        self.assertIsNotNone(data)
        self.assertEqual(len(data), settings.LOOKBACK_PERIOD)
        self.assertIn("close", data.columns)

    def test_fetch_latest_data(self):
        data = self.data_fetcher.fetch_latest_data()
        self.assertIsNotNone(data)
        self.assertIn("close", data.index)


if __name__ == "__main__":
    unittest.main()
