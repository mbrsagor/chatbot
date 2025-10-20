# app/chatbot.py
import json
import re
from typing import Optional

# A tiny knowledge base (could be moved to a JSON file)
FAQ = {
    "what is your name": "I'm PyBot — a sample Python chatbot.",
    "who made you": "You did! Or the developer of this tutorial did 😉",
    "help": "Ask me about 'features', 'run', or general questions like 'what is your name'.",
    "features": "This bot supports realtime chat, a simple FAQ, and saving conversation logs."
}

def normalize(text: str) -> str:
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()

def find_faq_response(msg: str) -> Optional[str]:
    q = normalize(msg)
    # exact match
    if q in FAQ:
        return FAQ[q]
    # simple fuzzy: check keywords
    for key, resp in FAQ.items():
        if set(key.split()).intersection(set(q.split())):
            return resp
    return None

def generate_response(message: str, context: dict = None) -> dict:
    """
    Very simple response generator:
    - check FAQ
    - pattern replies for greetings
    - fallback echo
    returns dict: { "reply": str, "intent": str }
    """
    ctx = context or {}
    text = message.strip()
    n = normalize(text)
    # greetings
    if n in ("hi", "hello", "hey", "hi there", "hello there"):
        return {"reply": "Hello! How can I help you today?", "intent": "greeting"}
    # thanks
    if any(tok in n for tok in ("thank", "thanks")):
        return {"reply": "You're welcome! Anything else?", "intent": "gratitude"}
    # FAQ
    faq = find_faq_response(text)
    if faq:
        return {"reply": faq, "intent": "faq"}
    # pattern: ask for run instructions
    if "run" in n and ("project" in n or "bot" in n or "how" in n):
        return {"reply": "Run `uvicorn app.main:app --reload` from project root, or use Docker as documented.", "intent": "run_instructions"}
    # fallback: echo + hint
    return {
        "reply": f"I heard: \"{text}\". I don't fully understand yet — try asking 'help' or 'features'.",
        "intent": "fallback"
    }

