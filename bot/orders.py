def build_order(symbol:str, side:str, order_type:str, qty:float, price=None):
    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": qty
    }

    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    return payload