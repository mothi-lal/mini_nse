import time
import random
import json
from engine.matching_engine import MatchingEngine

def run(n=20000):
    eng = MatchingEngine()
    t0 = time.time()

    for i in range(n):
        side = random.choice(["buy", "sell"])
        price = round(random.uniform(90, 110), 2)
        qty = random.randint(1, 10)
        eng.add_order(i, side, price, qty)

    t1 = time.time()
    duration = t1 - t0
    tpm = (n / duration) * 60

    out = {
        "orders": n,
        "time_sec": round(duration, 3),
        "trades_per_min": round(tpm, 1)
    }

    with open("benchmark_results.json", "w") as f:
        json.dump(out, f, indent=2)

    print(out)

if __name__ == "__main__":
    run()
