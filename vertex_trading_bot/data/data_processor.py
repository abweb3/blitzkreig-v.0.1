"""
Data Processor Module for Vertex Trading Bot
"""

from vertex_trading_bot.indicators.rsi import RSI
from vertex_trading_bot.indicators.stoch_rsi import StochRSI
from vertex_trading_bot.indicators.bollinger_bands import BollingerBands
from vertex_trading_bot.indicators.macd import MACD
from vertex_trading_bot.config import settings


class DataProcessor:
    def __init__(self):
        self.rsi = RSI(settings.RSI_PERIOD)
        self.stoch_rsi = StochRSI(
            settings.STOCH_RSI_PERIOD, settings.STOCH_RSI_K, settings.STOCH_RSI_D
        )
        self.bollinger_bands = BollingerBands(settings.BB_PERIOD, settings.BB_STD)
        self.macd = MACD(settings.MACD_FAST, settings.MACD_SLOW, settings.MACD_SIGNAL)

    def process_data(self, df):
        df["rsi"] = self.rsi.calculate(df["close"])
        df["stoch_rsi_k"], df["stoch_rsi_d"] = self.stoch_rsi.calculate(df["close"])
        df["bb_upper"], df["bb_middle"], df["bb_lower"] = (
            self.bollinger_bands.calculate(df["close"])
        )
        df["bb_percent"] = (df["close"] - df["bb_lower"]) / (
            df["bb_upper"] - df["bb_lower"]
        )
        df["macd"], df["macd_signal"], df["macd_hist"] = self.macd.calculate(
            df["close"]
        )
        return df
