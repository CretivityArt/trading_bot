from bot.logger import setup_logger
from binance.client import Client


class BinanceClientWrapper:
    def __init__(self, api_key, api_secret):
        self.logger = setup_logger()
        self.client = Client(api_key, api_secret,testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            self.logger.info(f"Placing Order: {symbol} {side} {order_type} {quantity} {price}")

            if order_type == "MARKET":
                response = self.client.futures_create_order(symbol=symbol,
                                                                 side=side,
                                                                 order_type=order_type,
                                                                 quantity=quantity,
                                                                 type="MARKET")
                self.logger.info(f"Response: {response}")
                return response
            if order_type == "LIMIT":
                response = self.client.futures_create_order(symbol=symbol,
                                                                 side=side,
                                                                 order_type=order_type,
                                                                 quantity=quantity,
                                                                 type="LIMIT",
                                                                 price=price,
                                                            timeInForce="GTC")
                self.logger.info(f"Response: {response}")
                return response
            if order_type == "STOP_MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="STOP_MARKET",
                    stopPrice=price,
                    closePosition=False,
                    quantity=quantity
                )
                self.logger.info(f"Response: {response}")
                return response
        except Exception as e:
            self.logger.error(str(e))
            raise
