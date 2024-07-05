"""
Data fetcher test Module
"""

import unittest
from unittest.mock import patch
import pandas as pd
from vertex_trading_bot.data.data_fetcher import DataFetcher


class TestDataFetcher(unittest.TestCase):
    def setUp(self):
        self.data_fetcher = DataFetcher()

    def test_fetch_historical_data_empty(self):
        with patch(
            "vertex_trading_bot.data.data_fetcher.pd.read_csv",
            return_value=pd.DataFrame(),
        ):
            data = self.data_fetcher.fetch_historical_data()
            self.assertEqual(len(data), 0)

    def test_fetch_historical_data_with_anomalies(self):
        data_with_anomalies = pd.DataFrame(
            {"close": [100, -100, 200, float("nan"), 300]}
        )
        with patch(
            "vertex_trading_bot.data.data_fetcher.pd.read_csv",
            return_value=data_with_anomalies,
        ):
            data = self.data_fetcher.fetch_historical_data()
            self.assertTrue(data["close"].isna().any())
            self.assertTrue((data["close"] < 0).any())


if __name__ == "__main__":
    unittest.main()
