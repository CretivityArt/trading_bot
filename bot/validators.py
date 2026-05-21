def symbol_validator(symbol):
    symbol = symbol.upper()
    if not symbol.endswith("USDT"):
        raise "Only Symbols with USDT is supported"
    return symbol


def side_validator(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise "Invalid Side, Side Must Be BUY or SELL"
    return side


def order_type_validator(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT","STOP_MARKET"]:
        raise "Order Type Must Be MARKET or LIMIT or Stop_Market"
    return order_type


def quantity_validator(quantity):
    quantity = float(quantity)
    if quantity <= 0:
        raise "quantity must be greater than 0"
    return quantity


def price_validator(price):
    return float(price) if price else None
