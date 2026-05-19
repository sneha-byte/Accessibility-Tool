
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"Received from client {client_id}: {data}")
        await websocket.send_text(f"Echo: {data}")