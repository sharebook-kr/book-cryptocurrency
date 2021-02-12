# Korbit Websocket Subscribe Example
import websockets
import asyncio 
import json
import datetime 
import pprint

async def korbit_ws_client():
    uri = "wss://ws.korbit.co.kr/v1/user/push"

    async with websockets.connect(uri) as websocket:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp() * 1000)

        subscribe_fmt = {
            "accessToken": None, 
            "timestamp": timestamp, 
            "event": "korbit:subscribe",
            "data": {
                "channels": ["ticker:btc_krw"]
            }
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            pprint.pprint(data)


async def main():
    await korbit_ws_client()

asyncio.run(main())
