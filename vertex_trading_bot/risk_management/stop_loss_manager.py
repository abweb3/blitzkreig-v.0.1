"""
Stop Loss Manager Module
"""

from vertex_protocol.utils.math import to_x18, from_x18
from vertex_trading_bot.config import settings


class StopLossManager:
    def calculate_stop_loss(self, entry_price, position_type):
        entry_price = from_x18(entry_price)
        if position_type == "long":
            return to_x18(entry_price * (1 - from_x18(settings.STOP_LOSS_PERCENT)))
        elif position_type == "short":
            return to_x18(entry_price * (1 + from_x18(settings.STOP_LOSS_PERCENT)))
        else:
            raise ValueError("Invalid position type")

    def update_stop_loss(self, current_price, stop_loss, position_type):
        current_price = from_x18(current_price)
        stop_loss = from_x18(stop_loss)
        if position_type == "long" and current_price > stop_loss:
            return to_x18(
                max(
                    stop_loss,
                    current_price * (1 - from_x18(settings.STOP_LOSS_PERCENT)),
                )
            )
        elif position_type == "short" and current_price < stop_loss:
            return to_x18(
                min(
                    stop_loss,
                    current_price * (1 + from_x18(settings.STOP_LOSS_PERCENT)),
                )
            )
        else:
            return to_x18(stop_loss)
