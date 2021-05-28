import config
import json
import numpy
import pprint
import talib
import websocket
import binance

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = "ETHUSD"
TRADE_QUANTITY = 0.01

closes = []

def on_open(ws):
    print("connection opened")


def on_close(ws):
    print("connection closed")


def on_message(ws, message):
    global closes

    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    pprint.pprint(is_candle_closed)
    candle_closed = candle['c']

    if is_candle_closed:
        pprint.pprint(candle_closed)
        closes.append(float(candle_closed))
        print(closes)

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()

