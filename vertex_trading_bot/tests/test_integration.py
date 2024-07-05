import unittest
from unittest.mock import patch
import pandas as pd
from vertex_trading_bot import TradingBot, DataFetcher, OrderManager


class TestTradingIntegration(unittest.TestCase):
    def test_full_trading_cycle(self):
        with patch.object(
            DataFetcher,
            "fetch_historical_data",
            return_value=pd.DataFrame({"close": range(50)}),
        ), patch.object(OrderManager, "execute_trade", return_value=True):
            bot = TradingBot()
            bot.initialize()
            bot.run()
            # Assuming 'run' method processes one cycle of fetching, processing, and trading
            self.assertTrue(bot.order_manager.last_order_result)


if __name__ == "__main__":
    unittest.main()
