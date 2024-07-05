import unittest
import pandas as pd
from vertex_trading_bot.strategies.multi_indicator_strategy import (
    MultiIndicatorStrategy,
)
from vertex_trading_bot.models.ml_model import MLModel


class TestStrategy(unittest.TestCase):
    def setUp(self):
        self.ml_model = MLModel(["rsi", "macd"], 30, 5)
        self.strategy = MultiIndicatorStrategy(self.ml_model)
        self.data = pd.DataFrame(
            {
                "close": range(100),
                "rsi": range(30, 130),
                "stoch_rsi_k": range(0, 100),
                "stoch_rsi_d": range(0, 100),
                "bb_percent": [0.5] * 100,
                "macd": range(-50, 50),
                "macd_signal": range(-40, 60),
            }
        )

    def test_generate_signal(self):
        signal = self.strategy.generate_signal(self.data)
        self.assertIn(signal, [-1, 0, 1])


if __name__ == "__main__":
    unittest.main()
