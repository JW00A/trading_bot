import uuid
import time

class MockBinanceClient:
    def place_order(self, symbol, side, order_type, quantity, price=None):
        return {
            "orderId": str(uuid.uuid4()),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity if order_type == "MARKET" else 0,
            "avgPrice": price if order_type == "LIMIT" else 100.0,
            "timestamp": int(time.time() * 1000)
        }
