def symbol(v:str):
    v=v.upper()
    if not v.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")
    return v

def side(v:str):
    v=v.upper()
    if v not in {"BUY","SELL"}:
        raise ValueError("Side must be BUY or SELL")
    return v

def order_type(v:str):
    v=v.upper()
    if v not in {"MARKET","LIMIT"}:
        raise ValueError("Type must be MARKET or LIMIT")
    return v

def quantity(v:str):
    q=float(v)
    if q<=0:
        raise ValueError("Quantity must be >0")
    return q

def price(v,otype):
    if otype=="LIMIT":
        if v is None:
            raise ValueError("LIMIT order requires price")
        p=float(v)
        if p<=0:
            raise ValueError("Price must be >0")
        return p
    return None