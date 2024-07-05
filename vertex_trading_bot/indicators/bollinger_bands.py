"""
Bollinger Bands Indicator
"""

import pandas as pd


class BollingerBands:
    def __init__(self, period, std_dev):
        self.period = period
        self.std_dev = std_dev

    def calculate(self, data):
        middle = data.rolling(self.period).mean()
        std = data.rolling(self.period).std()
        upper = middle + (std * self.std_dev)
        lower = middle - (std * self.std_dev)
        return upper, middle, lower
