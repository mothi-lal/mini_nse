import heapq
import time
from dataclasses import dataclass, field

@dataclass(order=True)
class Order:
    price: float
    timestamp: float
    order_id: int = field(compare=False)
    quantity: int = field(compare=False)
    side: str = field(compare=False)

class MatchingEngine:
    def __init__(self):
        self.buy_heap = []   # max-heap via negative price
        self.sell_heap = []  # min-heap

    def add_order(self, order_id, side, price, quantity):
        ts = time.time()
        if side == "buy":
            heapq.heappush(self.buy_heap, (-price, ts, Order(price, ts, order_id, quantity, side)))
        else:
            heapq.heappush(self.sell_heap, (price, ts, Order(price, ts, order_id, quantity, side)))
        return self.match()

    def match(self):
        trades = []
        while self.buy_heap and self.sell_heap:
            best_buy = -self.buy_heap[0][0]
            best_sell = self.sell_heap[0][0]
            if best_buy < best_sell:
                break

            _, _, buy = heapq.heappop(self.buy_heap)
            _, _, sell = heapq.heappop(self.sell_heap)

            qty = min(buy.quantity, sell.quantity)
            trades.append({
                "buy_id": buy.order_id,
                "sell_id": sell.order_id,
                "price": sell.price,
                "quantity": qty
            })
        return trades

