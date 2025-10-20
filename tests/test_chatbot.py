# tests/test_chatbot.py
from chatbot import generate_response

def test_greeting():
    r = generate_response("Hi")
    assert "Hello" in r["reply"]

def test_faq_match():
    r = generate_response("what is your name")
    assert "PyBot" in r["reply"] or "name" in r["reply"].lower()

def test_fallback():
    r = generate_response("some random text 12345")
    assert r["intent"] in ("fallback",)

