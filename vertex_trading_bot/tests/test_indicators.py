import unittest
import pandas as pd
from vertex_trading_bot.indicators.rsi import RSI
from vertex_trading_bot.indicators.stoch_rsi import StochRSI
from vertex_trading_bot.indicators.bollinger_bands import BollingerBands
from vertex_trading_bot.indicators.macd import MACD


class TestIndicators(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({"close": range(100)})

    def test_rsi(self):
        rsi = RSI(14)
        result = rsi.calculate(self.data["close"])
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 100)

    def test_stoch_rsi(self):
        stoch_rsi = StochRSI(14, 3, 3)
        k, d = stoch_rsi.calculate(self.data["close"])
        self.assertIsNotNone(k)
        self.assertIsNotNone(d)
        self.assertEqual(len(k), 100)
        self.assertEqual(len(d), 100)

    def test_bollinger_bands(self):
        bb = BollingerBands(20, 2)
        upper, middle, lower = bb.calculate(self.data["close"])
        self.assertIsNotNone(upper)
        self.assertIsNotNone(middle)
        self.assertIsNotNone(lower)
        self.assertEqual(len(upper), 100)

    def test_macd(self):
        macd = MACD(12, 26, 9)
        macd_line, signal_line, histogram = macd.calculate(self.data["close"])
        self.assertIsNotNone(macd_line)
        self.assertIsNotNone(signal_line)
        self.assertIsNotNone(histogram)
        self.assertEqual(len(macd_line), 100)


if __name__ == "__main__":
    unittest.main()
