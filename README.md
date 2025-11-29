# mini NSE — High-Performance Order Matching Engine

### Features
- Max-heap (buy) and min-heap (sell) order books
- ~20k orders matched in <1 second
- Trades/min benchmark included
- FastAPI-based order ingestion
- Docker container ready

### Run API
```bash
uvicorn api.server:app --reload
