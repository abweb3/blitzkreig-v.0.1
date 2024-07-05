"""
Stochastic RSI Indicator
"""

from vertex_trading_bot.indicators.rsi import RSI


class StochRSI:
    def __init__(self, period, k_period, d_period):
        self.period = period
        self.k_period = k_period
        self.d_period = d_period
        self.rsi = RSI(period)

    def calculate(self, data):
        rsi = self.rsi.calculate(data)
        stoch_rsi = (rsi - rsi.rolling(self.period).min()) / (
            rsi.rolling(self.period).max() - rsi.rolling(self.period).min()
        )
        k = stoch_rsi.rolling(self.k_period).mean()
        d = k.rolling(self.d_period).mean()
        return k, d
