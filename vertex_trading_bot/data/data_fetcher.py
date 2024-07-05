"""
Data Fetcher Module for Vertex Trading Bot
"""

import pandas as pd
from vertex_protocol.client import create_vertex_client
from vertex_trading_bot.config import settings


class DataFetcher:
    def __init__(self):
        self.client = create_vertex_client(ClientMode.MAINNET, settings.PRIVATE_KEY)

    def fetch_historical_data(self):
        candles = self.client.market.get_candles(
            product_id=settings.PRODUCT_ID,
            resolution=settings.TIMEFRAME,
            limit=settings.LOOKBACK_PERIOD,
        )
        df = pd.DataFrame(
            candles, columns=["timestamp", "open", "high", "low", "close", "volume"]
        )
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        return df.set_index("timestamp").sort_index()

    def fetch_latest_data(self):
        latest_candle = self.client.market.get_candles(
            product_id=settings.PRODUCT_ID, resolution=settings.TIMEFRAME, limit=1
        )[0]
        return pd.Series(
            latest_candle, index=["timestamp", "open", "high", "low", "close", "volume"]
        )
