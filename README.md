# Python Chatbot (FastAPI + WebSocket)

## Run locally
1. Create virtualenv:
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
2. Install:
   pip install -r requirements.txt
3. Run:
   uvicorn app.main:app --reload
4. Open browser: http://127.0.0.1:8000

## Run with Docker
docker-compose up --build

## Tests
pytest

## Extend
- Replace logic in app/chatbot.py with an OpenAI call or an ML NLU pipeline.
- Persist conversations to DB (sqlite/postgres).
