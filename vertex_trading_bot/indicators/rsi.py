"""
Relative Strength Index (RSI) Indicator
"""

import pandas as pd


class RSI:
    def __init__(self, period):
        self.period = period

    def calculate(self, data):
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
