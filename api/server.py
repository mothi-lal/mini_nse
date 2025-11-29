from fastapi import FastAPI
from pydantic import BaseModel
from engine.matching_engine import MatchingEngine
import time

app = FastAPI()
engine = MatchingEngine()

class OrderIn(BaseModel):
    order_id: int
    side: str     # "buy" or "sell"
    price: float
    quantity: int

@app.post("/order")
def add(order: OrderIn):
    trades = engine.add_order(order.order_id, order.side, order.price, order.quantity)
    return {"received": order, "trades": trades}

@app.get("/health")
def health():
    return {"status": "ok", "ts": time.time()}

