"""
This module contains the implementation of a trading bot using the Vertex Protocol.
"""

import time
from vertex_protocol.client import create_vertex_client, VertexClientMode
from vertex_trading_bot import (
    DataFetcher,
    DataProcessor,
    MLModel,
    MultiIndicatorStrategy,
    OrderManager,
    PositionSizer,
    StopLossManager,
    log_error,
    log_trade,
    settings,
)


class TradingBot:
    """
    A trading bot that interacts with the Vertex Protocol to perform trading operations.
    It utilizes market data to make trades based on a strategy defined by multiple indicators and machine learning predictions.
    """

    def __init__(self):
        """
        Initializes the trading bot by setting up the Vertex client and initializing all components necessary for the trading operations.
        """
        # Ensure the ClientMode.MAINNET is correctly handled if different in actual import
        self.client = create_vertex_client(
            VertexClientMode.MAINNET, settings.PRIVATE_KEY
        )
        self.data_fetcher = DataFetcher()
        self.data_processor = DataProcessor()
        self.ml_model = MLModel(
            settings.ML_FEATURES, settings.ML_LOOKBACK, settings.ML_PREDICTION_HORIZON
        )
        self.strategy = MultiIndicatorStrategy(self.ml_model)
        self.position_sizer = PositionSizer(self.client)
        self.stop_loss_manager = StopLossManager()
        self.order_manager = OrderManager(self.client)

    def initialize(self):
        """
        Initializes the trading bot by fetching historical data and training the machine learning model.
        """
        historical_data = self.data_fetcher.fetch_historical_data()
        processed_data = self.data_processor.process_data(historical_data)
        self.ml_model.train(processed_data)

    def run(self):
        """
        Starts the trading bot's main loop. It continually fetches the latest market data,
        processes that data, generates trading signals, and executes trades based on those signals.
        """
        self.initialize()
        while True:
            try:
                latest_data = self.data_fetcher.fetch_latest_data()
                processed_data = self.data_processor.process_data(latest_data)
                signal = self.strategy.generate_signal(processed_data)

                if signal != 0:
                    current_price = processed_data["close"].iloc[-1]
                    position_size = self.position_sizer.calculate_position_size(
                        current_price,
                        self.stop_loss_manager.calculate_stop_loss(
                            current_price, "long" if signal > 0 else "short"
                        ),
                    )

                    if signal > 0:
                        self.order_manager.place_market_order("buy", position_size)
                        log_trade("BUY", position_size, current_price)
                    else:
                        self.order_manager.place_market_order("sell", position_size)
                        log_trade("SELL", position_size, current_price)

                time.sleep(60)  # Wait for 1 minute before next iteration
            except Exception as e:
                log_error(f"Error in main loop: {str(e)}")
                time.sleep(60)  # Wait for 1 minute before retrying


if __name__ == "__main__":
    bot = TradingBot()
    bot.run()
