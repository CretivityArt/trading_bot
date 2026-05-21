from bot.client import BinanceClientWrapper
import argparse
from bot.validators import *

# PUT API AND SECRET KEY
api_key = "XXXXXXXX"
secret_key = "XXXXXX"


def main():
    client = BinanceClientWrapper(api_key, secret_key)
    # inputs
    print("-----------------------Trader Bot Ready For Action--------------- ")
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", required=True)
    parser.add_argument("--price")
    args = parser.parse_args()
    try:
        print("-----------------------CHECKING INPUTS--------------------------- ")
        symbol = symbol_validator(args.symbol)
        side = side_validator(args.side)
        order_type = order_type_validator(args.type)
        quantity = quantity_validator(args.qty)
        price = price_validator(args.price)
        order_type = order_type.upper()
        if order_type == "LIMIT":
            if price:
                print("-----------------------PLACING ORDER TYPE=LIMIT-------------------- ")
                result = client.place_order(symbol, side, "LIMIT", quantity, price)
                print("-------------------------ORDER PLACED--------------------------------")
                print("-------------------------ORDER SUMMERY------------------------------")
                print(result)
            else:
                raise ValueError("LIMIT ORDER requires Price")
        if order_type == "MARKET":
            print("----------------------PLACING ORDER TYPE=MARKET------------------ ")
            result = client.place_order(symbol, side, "MARKET", quantity)
            print("-------------------------ORDER PLACED---------------------------")
            print("-------------------------ORDER SUMMERY---------------------------")
            print(result)
        if order_type == "STOP_MARKET":
            print("----------------------PLACING ORDER TYPE=STOP_MARKET------------------ ")
            result = client.place_order(symbol, side, "MARKET", quantity)
            print("-------------------------ORDER PLACED---------------------------")
            print("-------------------------ORDER SUMMERY---------------------------")
            print(result)

    except Exception as e:
        print(f"Failed: {str(e)}")


if __name__ == "__main__":
    main()
