"""
Configuration settings for the Vertex Trading Bot.

This module contains all the configurable parameters used throughout the trading bot,
including API keys, trading parameters, indicator settings, and risk management values.
"""
import os

from dotenv import load_dotenv
from vertex_protocol.utils.math import to_x18

# Vertex Protocol settings
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PRODUCT_ID = 1  # Replace with the actual product ID you want to trade

# Trading parameters
SYMBOL = "ETH-PERP"
TIMEFRAME = "5m"
LOOKBACK_PERIOD = 100

# Indicator parameters
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
STOCH_RSI_PERIOD = 14
STOCH_RSI_K = 3
STOCH_RSI_D = 3
BB_PERIOD = 20
BB_STD = 2
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# Risk management
MAX_POSITION_SIZE = to_x18(0.1)  # 10% of account balance
STOP_LOSS_PERCENT = to_x18(0.02)  # 2% stop loss

# Performance targets
PROFIT_TARGET = to_x18(0.15)  # 15% profit target

# Machine learning
ML_FEATURES = ["rsi", "stoch_rsi_k", "stoch_rsi_d", "bb_percent", "macd", "macd_signal", "macd_hist"]
ML_LOOKBACK = 30
ML_PREDICTION_HORIZON = 5
