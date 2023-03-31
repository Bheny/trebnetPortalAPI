import websocket
import json
import datetime

def on_message(ws, message):
    message = json.loads(message) 
    msg = f"""
    ============= NEW MESSAGE ===========
     {message['data']}
    =====================================
     """
    print(msg)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket connected")
    subscribe_data = {
        "action": "subscribe_instance",
        "request_id": 22,
        "pk": 1  # Change this to the ID of the notification you want to observe
    }
    ws.send(json.dumps(subscribe_data))


# websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://localhost:8000/ws/notifications/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
ws.on_open = on_open
ws.run_forever()
