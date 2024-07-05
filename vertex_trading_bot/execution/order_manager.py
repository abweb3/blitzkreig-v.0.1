"""
Order Manager Module
"""

from vertex_protocol.contracts.types import DepositCollateralParams
from vertex_protocol.engine_client.types.execute import OrderParams, PlaceOrderParams
from vertex_protocol.utils.expiration import OrderType, get_expiration_timestamp
from vertex_protocol.utils.nonce import gen_order_nonce
from vertex_trading_bot.config import settings


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, side, amount):
        order_params = OrderParams(
            product_id=settings.PRODUCT_ID,
            side=side,
            amount=amount,
            expiration=get_expiration_timestamp(60),
            nonce=gen_order_nonce(),
            order_type=OrderType.MARKET,
        )
        place_order_params = PlaceOrderParams(
            sender=self.client.address,
            priv=self.client.signer,
            subaccount_id=0,
            fee_ratio=0,
        )
        return self.client.place_order(order_params, place_order_params)

    def place_limit_order(self, side, amount, price):
        order_params = OrderParams(
            product_id=settings.PRODUCT_ID,
            side=side,
            amount=amount,
            price=price,
            expiration=get_expiration_timestamp(60),
            nonce=gen_order_nonce(),
            order_type=OrderType.LIMIT,
        )
        place_order_params = PlaceOrderParams(
            sender=self.client.address,
            priv=self.client.signer,
            subaccount_id=0,
            fee_ratio=0,
        )
        return self.client.place_order(order_params, place_order_params)

    def cancel_order(self, order_id):
        return self.client.cancel_order(order_id)

    def get_open_orders(self):
        return self.client.get_open_orders(settings.PRODUCT_ID)

    def get_order_status(self, order_id):
        return self.client.get_order_status(order_id)
