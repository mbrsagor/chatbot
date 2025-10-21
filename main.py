# app/main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uuid
from .chatbot import generate_response
from .storage import append_message

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def send_personal_message(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)

manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    session_id = client_id  # for logging; in real app map to user
    try:
        while True:
            data = await websocket.receive_json()
            user_text = data.get("message", "")
            append_message(session_id, "user", user_text)

            # generate reply (synchronous simple function; OK here)
            bot_resp = generate_response(user_text, context={})
            reply_text = bot_resp["reply"]
            append_message(session_id, "bot", reply_text)

            # send reply
            await manager.send_personal_message({"sender": "bot", "message": reply_text, "meta": bot_resp}, websocket)
    except WebSocketDisconnect:
        manager.disconnect(client_id)
