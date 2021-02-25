import websockets
import asyncio 
import json

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:
        greeting = await websocket.recv()
        print(greeting)

        subscribe_fmt = {
            "type":"ticker", 
            "symbols": ["BTC_KRW"], 
            "tickTypes": ["1H"]
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)


async def main():
    await bithumb_ws_client()

asyncio.run(main())
