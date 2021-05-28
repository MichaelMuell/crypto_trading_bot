import config
import json
import numpy
import pprint
import talib
import websocket
import binance

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"


def on_open(ws):
    print("connection opened")


def on_close(ws):
    print("connection closed")


def on_message(ws, message):
    print("received message")
    print(message)

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
