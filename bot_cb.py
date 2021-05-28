import config
import json
import numpy
import pprint
import talib
from websocket import create_connection
import binance

URL = "wss://ws-feed.pro.coinbase.com"

ws = create_connection(URL)

params = {
    "type": "subscribe",
    "product_ids": [
        "ETH-USD"
    ],
    "channels": [
        "level2",
        "heartbeat",
        {
            "name": "ticker",
            "product_ids": [
                "ETH-USD"
            ]
        }
    ]
}

def single():
    ws.send(json.dumps(params))

    result = ws.recv()

    print(result)

single()