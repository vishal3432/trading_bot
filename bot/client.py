import time, hmac, hashlib, requests
from urllib.parse import urlencode
from .logging_config import setup_logger

BASE_URL = "https://testnet.binancefuture.com"
logger = setup_logger()

class BinanceClient:
    def __init__(self, api_key:str, api_secret:str):
        if not api_key or not api_secret:
            raise ValueError("API credentials missing")
        self.key = api_key
        self.secret = api_secret

    def _sign(self, params:dict):
        query = urlencode(params)
        signature = hmac.new(
            self.secret.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()
        return f"{query}&signature={signature}"

    def _headers(self):
        return {"X-MBX-APIKEY": self.key}

    def place_order(self, params:dict):
        params["timestamp"] = int(time.time()*1000)
        query = self._sign(params)
        url = f"{BASE_URL}/fapi/v1/order"

        logger.info(f"REQUEST → {params}")

        try:
            res = requests.post(url, headers=self._headers(), params=query, timeout=10)
            data = res.json()
        except requests.RequestException as e:
            logger.error(f"NETWORK ERROR → {e}")
            raise RuntimeError("Network error")

        logger.info(f"RESPONSE → {data}")

        if res.status_code != 200:
            raise RuntimeError(data)

        return data