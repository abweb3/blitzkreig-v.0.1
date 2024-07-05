"""
Position Sizer Module
"""

from vertex_protocol.utils.math import to_x18, from_x18
from vertex_trading_bot.config import settings


class PositionSizer:
    def __init__(self, client):
        self.client = client

    def calculate_position_size(self, entry_price, stop_loss_price):
        account_balance = from_x18(self.client.portfolio.get_balance())
        risk_amount = account_balance * from_x18(settings.MAX_POSITION_SIZE)
        risk_per_share = abs(entry_price - stop_loss_price)
        return to_x18(risk_amount / risk_per_share)
