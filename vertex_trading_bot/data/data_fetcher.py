"""
Data Fetcher Module for Vertex Trading Bot
"""

import pandas as pd
from vertex_protocol.client import create_vertex_client, VertexClientMode
from vertex_trading_bot.config import settings


class DataFetcher:
    """
    DataFetcher is responsible for fetching market data from the Vertex Protocol.

    It initializes a client connection to the Vertex Protocol 
    and provides methods to fetch historical and latest
    candlestick data for a given product.

    Attributes:
        client: An instance of VertexClient initialized with 
        the provided private key and set to MAINNET mode.
    """

    def __init__(self):
        """
        Initialize the DataFetcher with a Vertex client.

        The client is set to operate in the MAINNET mode 
        using the private key specified in the settings.
        """
        self.client = create_vertex_client(
            VertexClientMode.MAINNET, settings.PRIVATE_KEY
        )

    def fetch_historical_data(self):
        """
        Fetch historical candlestick data.

        This method retrieves historical market data based on 
        the product ID, resolution, and lookback period
        specified in the settings.

        Returns:
            DataFrame: A pandas DataFrame containing historical candlestick data 
            with columns for timestamp, open, high, low, close, and volume. 
            If an error occurs, an empty DataFrame is returned.
        """
        try:
            candles = self.client.market.get_candlesticks(
                params={
                    "product_id": settings.PRODUCT_ID,
                    "resolution": settings.TIMEFRAME,
                    "limit": settings.LOOKBACK_PERIOD,
                }
            )
            df = pd.DataFrame(
                candles, columns=["timestamp", "open", "high", "low", "close", "volume"]
            )
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
            return df.set_index("timestamp").sort_index()
        except ValueError as ve:
            print(f"ValueError fetching historical data: {ve}")
        except TypeError as te:
            print(f"TypeError fetching historical data: {te}")
        except Exception as e:
            print(f"Unexpected error fetching historical data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

    def fetch_latest_data(self):
        """
        Fetch the latest candlestick data.

        This method retrieves the most recent market data based on
        the product ID and resolution specified
        in the settings.

        Returns:
            Series: A pandas Series containing the latest candlestick data 
            with fields for timestamp, open, high, low, close, and volume.
            If an error occurs, an empty Series is returned.
        """
        try:
            latest_candle = self.client.market.get_candlesticks(
                params={
                    "product_id": settings.PRODUCT_ID,
                    "resolution": settings.TIMEFRAME,
                    "limit": 1,
                }
            )[0]
            return pd.Series(
                latest_candle,
                index=["timestamp", "open", "high", "low", "close", "volume"],
            )
        except ValueError as ve:
            print(f"ValueError fetching latest data: {ve}")
        except TypeError as te:
            print(f"TypeError fetching latest data: {te}")
        except Exception as e:
            print(f"Unexpected error fetching latest data: {e}")
        return pd.Series()  # Return an empty Series in case of an error
