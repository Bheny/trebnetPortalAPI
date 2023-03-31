import websocket
import json
import datetime

def on_message(ws, message):
    message = json.loads(message) 
    err = f"""
    ============= ERROR ===========
     {message['errors'][0]}
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     """
    msg = f"""
    ============= NEW MESSAGE ===========
     {message['data']}
    =====================================
     """
    if err is not None:
        print(err)
    else:
        print(msg)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket connected")
    subscribe_data = {
        "action": "join_room",
        "request_id": 22,
        "pk": 1  # Change this to the ID of the notification you want to observe
    }
    ws.send(json.dumps(subscribe_data))


# websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://localhost:8000/ws/chat/?Token=a1027804a6594e582affa7457b636f361f6006e10694fd4d1525c05035e4a40a",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
ws.on_open = on_open
ws.run_forever()
