"""
Moving Average Convergence Divergence (MACD) Indicator
"""

import pandas as pd


class MACD:
    def __init__(self, fast_period, slow_period, signal_period):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

    def calculate(self, data):
        ema_fast = data.ewm(span=self.fast_period, adjust=False).mean()
        ema_slow = data.ewm(span=self.slow_period, adjust=False).mean()
        macd = ema_fast - ema_slow
        signal = macd.ewm(span=self.signal_period, adjust=False).mean()
        hist = macd - signal
        return macd, signal, hist
