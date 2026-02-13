import argparse, os
from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.orders import build_order
from bot import validators as v

load_dotenv()

def main():
    parser=argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol",required=True)
    parser.add_argument("--side",required=True)
    parser.add_argument("--type",required=True)
    parser.add_argument("--quantity",required=True)
    parser.add_argument("--price")

    a=parser.parse_args()

    try:
        symbol=v.symbol(a.symbol)
        side=v.side(a.side)
        otype=v.order_type(a.type)
        qty=v.quantity(a.quantity)
        price=v.price(a.price,otype)

        print("\nORDER SUMMARY")
        print("--------------")
        print(symbol, side, otype, qty, price if price else "")

        client=BinanceClient(os.getenv("API_KEY"), os.getenv("API_SECRET"))
        payload=build_order(symbol,side,otype,qty,price)
        res=client.place_order(payload)

        print("\nRESPONSE")
        print("---------")
        for k in ["orderId","status","executedQty","avgPrice"]:
            print(f"{k}: {res.get(k)}")

        print("\nSUCCESS")

    except Exception as e:
        print("\nFAILED")
        print(e)

if __name__=="__main__":
    main()