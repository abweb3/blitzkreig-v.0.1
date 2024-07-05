"""
Multi-Indicator Trading Strategy
"""

from vertex_trading_bot.config import settings


class MultiIndicatorStrategy:
    def __init__(self, ml_model):
        self.ml_model = ml_model

    def generate_signal(self, data):
        rsi = data["rsi"].iloc[-1]
        stoch_rsi_k = data["stoch_rsi_k"].iloc[-1]
        stoch_rsi_d = data["stoch_rsi_d"].iloc[-1]
        bb_percent = data["bb_percent"].iloc[-1]
        macd = data["macd"].iloc[-1]
        macd_signal = data["macd_signal"].iloc[-1]

        ml_prediction = self.ml_model.predict(data.iloc[-1:])

        signal = 0

        if (
            rsi < settings.RSI_OVERSOLD
            and stoch_rsi_k < 20
            and stoch_rsi_d < 20
            and bb_percent < 0.2
            and macd > macd_signal
            and ml_prediction > 0
        ):
            signal = 1  # Buy signal
        elif (
            rsi > settings.RSI_OVERBOUGHT
            and stoch_rsi_k > 80
            and stoch_rsi_d > 80
            and bb_percent > 0.8
            and macd < macd_signal
            and ml_prediction < 0
        ):
            signal = -1  # Sell signal

        return signal
